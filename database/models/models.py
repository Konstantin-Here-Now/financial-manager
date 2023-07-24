from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer, String, Numeric, UUID, TIMESTAMP

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("email", String, nullable=False, unique=True),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
)

account = Table(
    "account",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("money", Numeric(12, 2)),
    Column("user_id", UUID, ForeignKey(user.c.id), unique=True),
)
