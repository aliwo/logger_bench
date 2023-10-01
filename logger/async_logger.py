from typing import Sequence

from logger.async_handler import AsyncHandler
from logger.log_level import LogLevel


class AsyncLogger:

    def __init__(self, log_level: LogLevel, handlers: Sequence[AsyncHandler] = None) -> None:
        self.log_level = log_level
        self.handlers = handlers or []

    async def _handle(self, message: str | bytes) -> None:
        for handler in self.handlers:
            await handler.handle(message)

    async def info(self, message: str | bytes) -> None:
        if self.log_level <= LogLevel.INFO:
            await self._handle(message)
