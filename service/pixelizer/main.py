from core.config import config
from core.logger import setting_logger, logger
from asyncio import run
import uvicorn


async def _main():
    uvicornConfig = uvicorn.Config()
    server = uvicorn.Server(uvicornConfig)
    server.run()


if __name__ == "__main__":
    logger.info('Start app')

    logger.info(f'config is{config.model_dump()}')

    setting_logger(config.env_type)
    logger.info('The logger is already set up')

    run(_main)
