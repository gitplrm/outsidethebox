from pathlib import Path
import duckdb

from config.settings import DATABASE_PATH


def create_database():

    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    conn = duckdb.connect(str(DATABASE_PATH))

    conn.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            ano_escolar VARCHAR,
            turma VARCHAR,
            matricula VARCHAR,
            nome VARCHAR,
            status VARCHAR
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS resultados_alunos (
            ano_escolar VARCHAR,
            turma VARCHAR,
            bimestre INTEGER,
            matricula VARCHAR,
            disciplina VARCHAR,
            percentual_acerto DOUBLE
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS questoes (
            ano_escolar VARCHAR,
            turma VARCHAR,
            bimestre INTEGER,
            disciplina VARCHAR,
            descritor VARCHAR,
            percentual_acerto DOUBLE,
            aula_url VARCHAR
        )
    """)

    conn.close()

    print("Banco criado com sucesso!")


if __name__ == "__main__":
    create_database()