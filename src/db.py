import os
import psycopg2
from psycopg2.extensions import connection, cursor


def get_db_conn() -> tuple[connection, cursor]:
    """Get Postgres connection and cursor


    Returns:
        tuple[connection, cursor]
    """
    conn = psycopg2.connect(
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST", "0.0.0.0"),
        port=os.environ.get("DB_PORT", 5432),
    )
    return conn, conn.cursor()
