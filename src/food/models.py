from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey
from typing import TYPE_CHECKING

from src.database import Base

if TYPE_CHECKING:
    from src.users.models import UserModel


class FoodModel(Base):
    __tablename__ = "foods"

    date: Mapped[str]
    calories: Mapped[int]
    protein: Mapped[int]
    carbohydrates: Mapped[int]
    fats: Mapped[int]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship(back_populates="food")
