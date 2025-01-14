
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
 pass


from sqlalchemy.orm import (
 Mapped,
 mapped_column
)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
 autocommit=False, autoflush=False, bind=engine
)

