from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, BigInteger
from typing import TYPE_CHECKING

from src.database import Base

if TYPE_CHECKING:
    from src.trains.models import TrainModel
    from src.food.models import FoodModel


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True)
    password: Mapped[bytes]
    first_name: Mapped[str] = mapped_column(String(64), nullable=True)
    last_name: Mapped[str] = mapped_column(String(64), nullable=True)

    trains: Mapped[list["TrainModel"]] = relationship(back_populates="user")
    food: Mapped[list["FoodModel"]] = relationship(back_populates="user")
