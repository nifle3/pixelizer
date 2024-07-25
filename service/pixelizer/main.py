from .core.config import config
from .core.logger import setting_logger, logger
from .routers.health import health_router
from .routers.v1.image import router as vone_image_router
from .routers.v1.login import router as vone_login_router
from .routers.v1.subscription import router as vone_subscription_router
from .routers.v1.user import router as vone_user_router
from fastapi import FastAPI


async def _main():
    logger.info('Start app')

    logger.info(f'config is{config.model_dump()}')

    setting_logger(config.env_type)
    logger.info('The logger is already set up')

    app = FastAPI()

    app.include_router(health_router)
    app.include_router(vone_image_router)
    app.include_router(vone_user_router)
    app.include_router(vone_subscription_router)
    app.include_router(vone_login_router)


if __name__ == "__main__":
    _main()
