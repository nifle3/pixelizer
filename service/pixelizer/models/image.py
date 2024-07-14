from uuid import UUID
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID as SQLUUID
from sqlalchemy import String, DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from base import Base


class Image(Base):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pixelize_image_link: Mapped[str] = mapped_column(String(255))
    source_image_link: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DATETIME)
    user_id = Mapped[UUID] = mapped_column(SQLUUID)
