import duckdb
from config.settings import DATABASE_PATH

conn = duckdb.connect(str(DATABASE_PATH))

print("DISCIPLINAS\n")

print(
    conn.execute("""
        SELECT DISTINCT disciplina
        FROM questoes
        ORDER BY disciplina
    """).fetchdf()
)

print("\nANOS ESCOLARES\n")

print(
    conn.execute("""
        SELECT DISTINCT ano_escolar
        FROM questoes
        ORDER BY ano_escolar
    """).fetchdf()
)

conn.close()