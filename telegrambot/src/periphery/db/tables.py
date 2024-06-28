from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"db.{type(self).__name__}(id={self.id!r})"


class User(Base):
    __tablename__ = "users"

    chat_id: Mapped[int]
