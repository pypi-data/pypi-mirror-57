import asyncio
import datetime
import hashlib
import logging
import os
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Callable, Optional, Awaitable

import bs4
import httpx
import sanic
from sanic.request import Request
from sanic.response import text
from sanic.server import AsyncioServer

logger = logging.getLogger("websub")


class HubNotFoundException(Exception):
    pass


@dataclass
class Subscription:
    hub: str
    topic: str
    hex_id: str

    handler: Callable[[bytes], Awaitable[None]]

    verified_at: Optional[datetime.datetime] = None
    lease: Optional[datetime.timedelta] = None

    cold: bool = True

    def __repr__(self) -> str:
        return f"<Subscription {self.topic} (0x{self.hex_id.upper()} {self.lease})>"


class UnknownFeedStrategy(Enum):
    Ignore = auto()
    Unsubscribe = auto()


class WebSubClient:
    def __init__(self, https: bool, app: sanic.Sanic, server: str = None, _from: str = None,
                 unknown_feed_strategy: UnknownFeedStrategy = UnknownFeedStrategy.Ignore):
        self.server = server
        self.https = https
        self.app = app
        self.u_feed_strat = unknown_feed_strategy
        self._from = f"{_from or 'default'} (pywebsub)"
        self.running = False
        self.subscriptions: Dict[str, Subscription] = {}
        self.seen_hashes = set()
        self.heartbeat_hashes = set()

    async def subscribe(self, hub: str, topic: str, handler: Callable[[bytes], Awaitable[None]]):
        s = Subscription(hub=hub,
                         topic=topic,
                         hex_id=os.urandom(16).hex(),
                         handler=handler)
        self.subscriptions[topic] = s
        if self.running:
            s.cold = False
            await self.make_request(s)

    async def unsubscribe(self, topic: str):
        sub = self.subscriptions.get(topic)
        if sub is None:
            logger.warning(f"Unsubscribe requested for {topic}, but subscription does not exist.")
        else:
            if self.running:
                await self.make_request(sub, "unsubscribe")
            del self.subscriptions[topic]

    async def _try_subsubscribe(self, request: Request, hex_id: str):
        soup = bs4.BeautifulSoup(request.body, "xml")
        selflink = soup.find("link", rel="self")
        if selflink is None:
            logger.warning(f"Cannot unsubscribe incoming subscription at {hex_id}; "
                           f"rel=self link is not found.")
            return
        topic = selflink.attrs['href']
        hublink = soup.find("link", rel="hub")
        if hublink is None:
            try:
                hub = await self.discover(topic)
            except HubNotFoundException:
                logger.warning(f"Cannot unsubscribe incoming subscription at {hex_id} for {topic}; "
                               f"rel=hub not found and discover errored.")
                return
        else:
            hub = hublink.attrs['href']

        await self._make_request(topic=topic, hub=hub, callback_url=self.make_callback_url(hex_id), mode="unsubscribe")

    async def discover(self, topic: str) -> str:
        try:
            resp = await httpx.get(topic, headers=self.headers)
        except httpx.exceptions.HTTPError as e:
            logger.exception(f"{topic} discovery request failed with exception:")
            raise HubNotFoundException(e)

        if resp.status_code not in range(200, 300):
            raise HubNotFoundException(f"{topic} discovery request failed, status is {resp.status_code}")
        else:
            logger.debug(f"{topic} discovery request succeeded")
            soup = bs4.BeautifulSoup(resp.content, "xml")
            link = soup.find("link", rel="hub")
            if link is None:
                raise HubNotFoundException(f"rel=hub link not present in {topic}")

            return link.attrs['href']

    async def discover_and_sub(self, topic: str, handler: Callable[[bytes], Awaitable[None]]):
        hub = await self.discover(topic)
        await self.subscribe(hub, topic, handler)

    async def make_request(self, sub: Subscription, mode: str = "subscribe"):
        callback_url = self.make_callback_url(sub.hex_id)
        await self._make_request(sub.topic, sub.hub, callback_url, mode, sub)

    async def _make_request(self, topic: str, hub: str, callback_url: str, mode: str,
                            subscription: Optional[Subscription] = None):

        logger.info(f"Doing {mode} request to {hub} for {topic}, calling back to {callback_url}")

        values = {
              "hub.callback": callback_url,
              "hub.topic":    topic,
              "hub.mode":     mode
        }

        try:
            resp = await httpx.post(hub, data=values, headers=self.headers)
        except httpx.exceptions.HTTPError:
            logger.exception(f"{mode} request failed with exception, {subscription!r} at {callback_url}:")
            return

        if resp.status_code != 202:
            logger.error(f"{mode} request failed, {subscription!r} at {callback_url}, status is {resp.status_code}")
        else:
            logger.info(f"{mode} request succeeded, {subscription!r} at {callback_url}")

    def make_callback_url(self, hex_id: str) -> str:
        return self.url_for('callback', hex_id=hex_id)

    def url_for(self, view_name: str, **kwargs):
        return self.app.url_for(f"websub.{view_name}", **kwargs,
                                _scheme='https' if self.https else 'http',
                                _external=True, _server=self.server)

    def get_sub_by_hex(self, hex_id: str) -> Optional[Subscription]:
        for s in self.subscriptions.values():
            if s.hex_id.lower() == hex_id.lower():
                return s

    async def broadcast(self, sub: Subscription, req: Request):
        body: bytes = req.body
        h: bytes = hashlib.md5(req.body).digest()
        if h not in self.seen_hashes:
            self.seen_hashes.add(h)
            await sub.handler(body)
        else:
            logger.info(f"Update for {sub} already handled, hash is {h.hex()}")

    @property
    def bp(self) -> sanic.Blueprint:
        bp = sanic.Blueprint("websub")

        @bp.route("/hb/<hex_id>")
        async def heartbeat(request: Request, hex_id: str) -> sanic.response.HTTPResponse:
            return text(hex_id, status=200 if hex_id in self.heartbeat_hashes else 404)

        @bp.route("/push-callback/<hex_id>", methods=["GET", "POST"])
        async def callback(request: Request, hex_id: str) -> sanic.response.HTTPResponse:
            topic = request.args.get("hub.topic")
            mode = request.args.get("hub.mode")

            if mode == "subscribe":
                sub = self.subscriptions.get(topic)
                if sub is None:
                    logger.warning(f"Unexpected subscription for {topic} on {hex_id}")
                    return text("Unexpected subscription", status=400)
                else:
                    lease_s = request.args.get('hub.lease_seconds')
                    if not lease_s:
                        logger.error(f"Lease is not resolved for sub {sub}: {lease_s!r}")
                        return text("No lease", status=400)
                    sub.verified_at = datetime.datetime.now()
                    sub.lease = datetime.timedelta(seconds=int(lease_s))
                    logger.info(f"Subscription verified for {sub}, lease is {sub.lease}")
                    if hex_id != sub.hex_id:
                        logger.warning(f"Subscription hex does not match path hex: {sub.hex_id} != {hex_id}")
                    return text(request.args.get("hub.challenge"))

            elif mode == "unsubscribe":
                sub = self.subscriptions.get(topic)
                if sub is None:
                    logger.warning(f"Unexpected unsubscribe for {topic} on {hex_id}, still unsubscribing...")
                    return text(request.args.get("hub.challenge"))
                else:
                    logger.info(f"Unsubscribe confirmed for {topic} on {hex_id}")
                    if hex_id != sub.hex_id:
                        logger.warning(f"Subscription hex does not match path hex: {sub.hex_id} != {hex_id}")
                    return text(request.args.get("hub.challenge"))

            elif mode == "denied":
                logger.warning(f"Subscription denied for {topic}, reason was {request.args.get('hub.reason')}")
                return sanic.response.HTTPResponse()
                # TODO: Don't do anything for now, should probably mark the subscription.
            else:
                sub = self.get_sub_by_hex(hex_id)
                if sub is None:
                    logger.warning("Got unknown message for unknown subscription:")
                    logger.warning(f"{hex_id}: {request}")
                    if self.u_feed_strat == UnknownFeedStrategy.Unsubscribe:
                        logger.info('Unknown feed strategy is "unsubscribe"; unsubscribing from unknown feed...')
                        await self._try_subsubscribe(request, hex_id)
                    return text("Unknown subscription", status=400)
                else:
                    logger.info(f"Update for {sub}")
                    await self.broadcast(sub, request)
                    return sanic.response.HTTPResponse()

        return bp

    @property
    def headers(self):
        return {
              "From": self._from
        }

    def install(self):
        bp = self.bp
        if bp.name not in self.app.blueprints:
            self.app.blueprint(self.bp)

    async def boot(self, *args, add_worker=True, return_asyncio_server=True, **kwargs) -> Optional[AsyncioServer]:
        if add_worker:
            self.app.add_task(self.start_worker)
        return await self.app.create_server(*args, **kwargs, return_asyncio_server=return_asyncio_server)

    async def stop(self):
        self.app.stop()

    async def start_worker(self):
        self.running = True
        self.install()
        logger.debug("waiting 5 seconds before starting checking wait_till_heartbeat...")
        await asyncio.sleep(5)
        logger.debug("waiting till heartbeat...")
        await self.wait_till_heartbeat()
        logger.debug("starting subbed loop...")
        await self.ensure_subbed_loop()

    async def wait_till_heartbeat(self):
        class NotCorrect(Exception):
            pass

        while True:
            try_hex = os.urandom(6).hex()
            self.heartbeat_hashes.add(try_hex)
            try:
                r = await httpx.get(self.url_for("heartbeat", hex_id=try_hex))
                if r.status_code != 200:
                    raise NotCorrect()
            except httpx.exceptions.HTTPError:
                logger.debug("heartbeat failed with HTTPError, waiting 2 seconds...")
                await asyncio.sleep(2)
            except NotCorrect:
                logger.debug("heartbeat failed reaching current server, waiting 2 seconds...")
                await asyncio.sleep(2)
            else:
                return
            finally:
                self.heartbeat_hashes.remove(try_hex)

    async def ensure_subbed_loop(self):
        while True:
            try:
                await self.ensure_subbed()
            except Exception:
                logger.exception("ensure_subbed gave an exception")

            await asyncio.sleep(60)

    async def ensure_subbed(self):
        logger.debug("ensure_subbed called")
        in_one_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
        for s in self.subscriptions.values():
            logger.debug(f"ensure_subbed: checking {s}")
            if not s.cold and (s.verified_at is None or s.lease is None):
                logger.debug(f"ensure_subbed: {s} not yet verified, skipping...")
                continue
            if s.cold or (s.verified_at + s.lease) < in_one_hour:
                s.cold = False
                await self.make_request(s)
            else:
                logger.debug(f"ensure_subbed: {s} does not need new lease, verified at {s.verified_at}")
