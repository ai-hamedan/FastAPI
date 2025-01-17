# from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

class User(Base):
 __tablename__ = "user"
 id: Mapped[int] = mapped_column(
 primary_key=True,
 )
 name: Mapped[str]
 email: Mapped[str]
