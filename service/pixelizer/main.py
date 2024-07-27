from contextlib import asynccontextmanager
from .core.config import config
from .core.logger import setting_logger, logger
from .routers.health import health_router
from .routers.v1.image import router as vone_image_router
from .routers.v1.login import router as vone_login_router
from .routers.v1.subscription import router as vone_subscription_router
from .routers.v1.user import router as vone_user_router
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Start app')

    logger.info(f'config is{config.model_dump()}')

    setting_logger(config.env_type)

    logger.info('The logger is already set up')

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(health_router)
app.include_router(vone_image_router, prefix="/v1")
app.include_router(vone_user_router, prefix="/v1")
app.include_router(vone_subscription_router, prefix="/v1")
app.include_router(vone_login_router, prefix="/v1")
