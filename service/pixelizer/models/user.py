from uuid import UUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as SQLUUID
from base import Base


class User(Base):
    __tablename_ = "users"

    id: Mapped[UUID] = mapped_column(SQLUUID, primary_key=True)
    nickname: Mapped[str] = mapped_column(String(255), unique=True)
    profile_image: Mapped[str] = mapped_column(String(255))
    keycloack_id: Mapped[UUID] = mapped_column(SQLUUID, unique=True)
