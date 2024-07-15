from uuid import UUID
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID as SQLUUID
from sqlalchemy import String, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base
from user import User


class Image(Base):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pixelize_image_link: Mapped[str] = mapped_column(String(255))
    source_image_link: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DATETIME)
    user_id = Mapped[UUID] = mapped_column(SQLUUID, ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="images")
