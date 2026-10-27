import duckdb

from config.settings import DATABASE_PATH


def get_connection():

    return duckdb.connect(
        str(DATABASE_PATH)
    )