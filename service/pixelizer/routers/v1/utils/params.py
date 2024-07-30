from typing_extensions import Annotated
from pydantic import BaseModel, Field


class Paginator(BaseModel):

    skip: Annotated[int, Field(
        ge=0
    )] = 0

    limit: Annotated[int, Field(
        ge=1
    )] = 1
