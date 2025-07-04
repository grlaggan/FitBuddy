from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum, String
from sqlalchemy.sql.schema import ForeignKey

from src.database.base import Base
from src.core import TrainStatus

if TYPE_CHECKING:
    from src.database import UserModel


class TrainModel(Base):
    __tablename__ = "trains"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str]
    type: Mapped[TrainStatus] = mapped_column(Enum(TrainStatus, native_enum=True))
    title: Mapped[str] = mapped_column(String(128))
    repeats: Mapped[int] = mapped_column(nullable=True)
    approaches: Mapped[int] = mapped_column(nullable=True)
    duration: Mapped[int] = mapped_column(nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship(back_populates="trains")
