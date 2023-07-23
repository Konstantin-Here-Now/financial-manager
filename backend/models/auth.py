from datetime import datetime
import uuid

from typing_extensions import Annotated
from decimal import Decimal

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, UUID, TIMESTAMP, Numeric

# for often usage
id_pk = Annotated[str, mapped_column(UUID, primary_key=True, default=uuid.UUID)]


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[id_pk]
    email: Mapped[str] = mapped_column(String(30), unique=True)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    password: Mapped[str] = mapped_column()

    # relationship
    money_account: Mapped["MoneyAccount"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"


class MoneyAccount(Base):
    __tablename__ = "money_account"

    id: Mapped[id_pk]
    money_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))

    # relationship
    user_id: Mapped[id_pk] = mapped_column(ForeignKey("user.id"))
    parent: Mapped["User"] = relationship(back_populates="money_account")

    def __repr__(self) -> str:
        return f"MoneyAccount(id={self.id!r}, money_amount={self.money_amount!r})"
