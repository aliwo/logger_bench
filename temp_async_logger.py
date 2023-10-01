from logger.async_handler import AsyncStreamHandler
from logger.async_logger import AsyncLogger
from logger.log_level import LogLevel


async def asset_logger_logs():
    logger = AsyncLogger(
        log_level=LogLevel.INFO,
        handlers=(
            AsyncStreamHandler(),
        )
    )

    await logger.info("안녕 이건 로거야")


async def asset_logger_does_not_logs_when_log_level_is_not_satisfied():
    logger = AsyncLogger(
        log_level=LogLevel.ERROR,
        handlers=(
            AsyncStreamHandler(),
        )
    )

    await logger.info("이건 로깅 안되. 로그레벨이 낮으니까")


if __name__ == "__main__":
    import asyncio

    asyncio.run(asset_logger_logs())

