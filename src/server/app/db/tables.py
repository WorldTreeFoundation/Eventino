import sqlalchemy

from .connection import DATABASE_URL

metadata = sqlalchemy.MetaData()
"""SQL metadata"""

# Events table
events = sqlalchemy.Table(
    "events",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer, sqlalchemy.Sequence("event_id_seq"),
        primary_key=True
    ),
    sqlalchemy.Column(
        "title",
        sqlalchemy.VARCHAR(100),
        nullable=False,
    ),
    sqlalchemy.Column(
        "guest_limit",
        sqlalchemy.Integer,
        nullable=False,
    ),
    sqlalchemy.Column(
        "info",
        sqlalchemy.Text,
    ),
    sqlalchemy.Column(
        "active",
        sqlalchemy.Boolean,
        nullable=False,
    ),
)
"""Events table
"""

# Create tables
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
