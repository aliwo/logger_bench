import logging
import sys

from fastapi import FastAPI

from consts import LOG_MESSAGE
from logger.async_handler import AsyncStreamHandler
from logger.async_logger import AsyncLogger
from logger.log_level import LogLevel

app = FastAPI()


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))
logger.setLevel(logging.INFO)


@app.get("/sync")
async def root():
    logger.info(LOG_MESSAGE)
    logger.info(LOG_MESSAGE)
    logger.info(LOG_MESSAGE)
    return {"message": "Hello World"}


async_logger = AsyncLogger(
    log_level=LogLevel.INFO,
    handlers=(
        AsyncStreamHandler(),
    )
)


@app.get("/async")
async def say_hello():
    await async_logger.info(LOG_MESSAGE)
    await async_logger.info(LOG_MESSAGE)
    await async_logger.info(LOG_MESSAGE)
    return {"message": f"Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
