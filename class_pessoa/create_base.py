from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped

from sqlalchemy import String
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "pessoa"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    idade: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f"User(id={self.id!r}, nome={self.nome!r}, idade={self.idade!r}, email={self.email!r}, senha= {self.senha!r})"