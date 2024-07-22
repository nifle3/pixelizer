from typing import List
from uuid import UUID
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as SQLUUID
from base import Base
from image import Image


class User(Base):
    __tablename_ = "users"

    id: Mapped[UUID] = mapped_column(SQLUUID, primary_key=True)
    nickname: Mapped[str] = mapped_column(String(255), unique=True)
    profile_image: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    keycloack_id: Mapped[UUID] = mapped_column(SQLUUID, unique=True)
    images: Mapped[List[Image]] = relationship(back_populates="user",
                                               cascade="all, delete-orphan")
