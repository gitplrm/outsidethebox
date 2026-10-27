import duckdb

from config.settings import DATABASE_PATH

def load_dataframe(
    df,
    table_name
):

    conn = duckdb.connect(
        str(DATABASE_PATH)
    )

    conn.register(
        "tmp_df",
        df
    )

    conn.execute(
        f"""
        INSERT INTO {table_name}
        SELECT *
        FROM tmp_df
        """
    )

    conn.close()

