# etl/audit.py

import duckdb
from config.settings import DATABASE_PATH

conn = duckdb.connect(str(DATABASE_PATH))

print(
    conn.execute("""
        SELECT
            COUNT(*) total,
            COUNT(DISTINCT matricula) unicos
        FROM alunos
    """).fetchdf()
)

conn.close()