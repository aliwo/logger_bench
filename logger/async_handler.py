import asyncio
import sys
from asyncio import StreamWriter
from io import TextIOWrapper
from typing import Optional


class AiologgerProtocol(asyncio.Protocol):
    async def _drain_helper(self):  # 이게 없으면 에러나던데... 이게 뭐하는거여?
        pass


class AsyncHandler:

    async def handle(self, message: str | bytes):
        pass


class AsyncStreamHandler(AsyncHandler):
    """
    aiologger 를 참고해서 만들었습니다.
    pip install aiologger
    """

    def __init__(self, stream: TextIOWrapper = sys.stdout) -> None:
        self._initialization_lock = asyncio.Lock()
        self.writer: Optional[StreamWriter] = None
        self.stream = stream

    async def _init_writer(self) -> None:
        async with self._initialization_lock:
            if self.writer is not None:
                return

            loop = asyncio.get_event_loop()

            transport, protocol = await loop.connect_write_pipe(
                AiologgerProtocol, self.stream
            )

            self.writer = StreamWriter(  # type: ignore # https://github.com/python/typeshed/pull/2719
                transport=transport, protocol=protocol, reader=None, loop=loop
            )

    async def handle(self, message: str | bytes) -> None:
        if self.writer is None:
            await self._init_writer()

        message = message if isinstance(message, bytes) else message.encode()

        self.writer.write(message)
        await self.writer.drain()
        # 와.. 콘솔에 hihi 가 찍힌다. 근데 원리를 모르겠음. connect_write_pipe 가 뭐임?

