from sys import stdout
from typing import Final
from env_type import EnvTypeEnum
from loguru import logger


_FORMAT: Final[str] = '{time} {level} {message}'


def setting_logger(env_type: EnvTypeEnum) -> None:
    logger.remove()

    match env_type:
        case EnvTypeEnum.dev:
            logger.add(stdout, format=_FORMAT, level='DEBUG')
        case EnvTypeEnum.prod:
            logger.add(stdout, format=_FORMAT, level='INFO',
                       serialize=True)
