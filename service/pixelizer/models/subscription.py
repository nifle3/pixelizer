from uuid import UUID
from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as SQLUUID
from .base import Base
from .user import User


class Subscription(Base):
    __tablename_ = "subscriptions"

    id: Mapped[UUID] = mapped_column(SQLUUID(as_uuid=True), primary_key=True)
    user_id: Mapped[UUID] = mapped_column(SQLUUID(as_uuid=True),
                                          ForeignKey("users.id"))
    follower_id: Mapped[UUID] = mapped_column(SQLUUID(as_uuid=True),
                                              ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(20))

    user: Mapped[List[User]] = relationship(back_populates="followers",
                                            foreign_keys=[user_id])
    follower: Mapped[List[User]] = relationship(back_populates="following",
                                                foreign_keys=[follower_id])
