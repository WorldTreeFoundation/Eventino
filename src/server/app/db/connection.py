import os
import databases

from config import (
    DB_NAME, DB_USER, DB_PASSWORD,
    DB_HOST, DB_PORT, DB_HOST_DEFAULT, DB_PORT_DEFAULT,
)

# Connection string
db_name = os.environ.get(DB_NAME)
user = os.environ.get(DB_USER)
password = os.environ.get(DB_PASSWORD)
host = os.environ.get(DB_HOST, DB_HOST_DEFAULT)
port = os.environ.get(DB_PORT, DB_PORT_DEFAULT)
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

database = databases.Database(DATABASE_URL)
"""Database object
"""
