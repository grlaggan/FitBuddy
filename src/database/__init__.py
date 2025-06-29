__all__ = ["Base", "init_db"]

from .init import InitDB
from .base import Base

init_db = InitDB()
