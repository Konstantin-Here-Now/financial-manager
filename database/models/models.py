from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer, String, Numeric, DateTime

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", String, primary_key=True),
    Column("email", String(60), nullable=False, unique=True),
    Column("username", String(60), nullable=False),
    Column("password", String(60), nullable=False),
    Column("registered_at", DateTime, default=datetime.utcnow),
)

account = Table(
    "account",
    metadata,
    Column("id", String, primary_key=True),
    Column("money", Numeric(12, 2)),
    Column("user_id", String, ForeignKey(user.c.id), unique=True),
)


category = Table(
    "category",
    metadata,
    Column("id", String, primary_key=True),
    Column("name", String(60), nullable=False),
    Column("user_id", String, ForeignKey(user.c.id)),
)

transaction = Table(
    "transaction",
    metadata,
    Column("id", String, primary_key=True),
    Column("operation", String(30), nullable=False),
    Column("amount", Numeric(12, 2)),
    Column("date", DateTime, default=datetime.utcnow),
    Column("user_id", String, ForeignKey(user.c.id)),
    Column("category_id", String, ForeignKey(category.c.id))
)

regular_transaction = Table(
    "regular_transaction",
    metadata,
    Column("id", String, primary_key=True),
    Column("operation", String(20), nullable=False),
    Column("amount", Numeric(12, 2), nullable=False),
    Column("regularity", String(20), nullable=False),
    Column("end_date", DateTime),
    Column("user_id", String, ForeignKey(user.c.id)),
)
