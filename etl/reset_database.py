import duckdb

from config.settings import DATABASE_PATH


def reset_database():

    conn = duckdb.connect(str(DATABASE_PATH))

    conn.execute("DROP TABLE IF EXISTS alunos")
    conn.execute("DROP TABLE IF EXISTS resultados_alunos")
    conn.execute("DROP TABLE IF EXISTS questoes")

    conn.close()

    print("Tabelas removidas.")
    

if __name__ == "__main__":
    reset_database()