import os
import psycopg2
from psycopg2.extensions import connection, cursor

from config import (
    DB_NAME, DB_USER, DB_PASSWORD,
    DB_HOST, DB_PORT, DB_HOST_DEFAULT, DB_PORT_DEFAULT,
)


def get_db_conn() -> tuple[connection, cursor]:
    """Get Postgres connection and cursor


    Returns:
        tuple[connection, cursor]
    """
    conn = psycopg2.connect(
        database=os.environ.get(DB_NAME),
        user=os.environ.get(DB_USER),
        password=os.environ.get(DB_PASSWORD),
        host=os.environ.get(DB_HOST, DB_HOST_DEFAULT),
        port=os.environ.get(DB_PORT, DB_PORT_DEFAULT),
    )
    return conn, conn.cursor()
