import asyncio
from collections import OrderedDict
from logging import getLogger
from json import loads, dumps, JSONDecodeError
from datetime import datetime

from websockets.exceptions import ConnectionClosed

from .protocol import CommandsMixin, Message
from .exceptions import RemoteMessageHandlerError, InternalMessageHandlerError

logger = getLogger(__name__)


class WebsocketHandlerBase:
    """Define protocol for communication between web client and server."""

    read_timeout = NotImplemented
    allowed_commands = NotImplemented

    def __init__(self, redis, websocket, channel_names, channel_patterns, read_timeout=None):
        self.websocket = websocket
        self.redis = redis
        self.channel_names = channel_names
        self.channel_patterns = channel_patterns
        self.read_timeout = read_timeout or self.read_timeout

        self.queue = asyncio.Queue()

        self.filters = OrderedDict()
        self.subscriptions = set()

    async def _websocket_reader(self):
        try:
            while True:
                await self.queue.put(Message(
                    source='websocket', content=await self.websocket.recv()))
        except ConnectionClosed:
            logger.debug("Connection was closed by client %s",
                         self.websocket.remote_address)

    def _apply_filters(self, message):
        """Return (passed, result)-tuple.

        Runs all filters in self.filters on the deserialized message and
        returns a boolean indicating whether all filters passed and a JSON
        string with the (modified) result.
        """
        if message is None:
            return False, None

        try:
            data = loads(message)
        except JSONDecodeError as e:
            raise InternalMessageHandlerError(
                "Decoding '{}' failed.".format(message)) from e

        passes = all((func(data) for func in self.filters.values()))
        return passes, data

    async def _queue_reader(self):
        source, message = await asyncio.wait_for(
            self.queue.get(), self.read_timeout)
        if source == 'websocket':
            await self._handle_remote_message(message)
        else:
            passes, data = self._apply_filters(message)
            if passes:
                await self._send(source, data)

    async def _send(self, source, data, client_reference=None):
        await self.websocket.send(dumps(dict(
            source=source,
            content=data,
            timestamp=datetime.now().timestamp() * 1000,  # how JS expects it
            client_reference=client_reference
        )))

    async def _handle_remote_message(self, message):
        try:
            command, *args = message.split()
            if command not in self.allowed_commands:
                # Don't even echo it back, most likely it's spam!
                logger.info("Got unknown command '%s' from %s!",
                            command, self.websocket.remote_address)
                return
            logger.debug("Processing command '%s' with args %s from %s.",
                         command, args, self.websocket.remote_address)
            await getattr(
                self, '_handle_{}_command'.format(command.lower()))(*args)
        except Exception as e:
            raise RemoteMessageHandlerError(
                "Handling message '{}' failed: {}".format(message, e)) from e

    def _channel_in_patterns(self, channel_name):
        return any(
            # [:-1] because the patterns have a `*` at the end
            pattern[:-1] in channel_name
            for pattern in self.channel_patterns
        )

    @classmethod
    async def create(cls, redis, websocket, channel_names, channel_patterns, read_timeout=None):
        """Create a handler instance setting up tasks and queues."""
        self = cls(redis, websocket, channel_names, channel_patterns, read_timeout=read_timeout)
        self.consumer_task = asyncio.ensure_future(self._websocket_reader())
        return self

    async def listen(self):
        """Read and handle messages from internal message queue.

        This coroutine blocks for up to self.read_timeout seconds.
        """
        await self._send('websocket', {'status': 'open'})
        while not self.consumer_task.done():
            try:
                await self._queue_reader()
            except asyncio.TimeoutError:
                if not self.websocket.open:
                    raise

    async def close(self):
        """Close all connections and cancel all tasks."""
        asyncio.wait_for(  # attempt to say goodbye to the client
            self.websocket.close(), self.read_timeout)
        self.consumer_task.cancel()


class WebsocketHandler(WebsocketHandlerBase, CommandsMixin):
    """Provides a Redis proxy to predefined channels"""

    read_timeout = 30
    allowed_commands = 'SUB', 'DEL', 'PING', 'GET'
