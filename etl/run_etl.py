from pathlib import Path

import duckdb
import pandas as pd

todos_alunos = []

from config.settings import (
    RAW_DATA_DIR,
    DATABASE_PATH
)

from etl.create_database import (
    create_database
)

from etl.extract import (
    read_br,
    read_bq
)

from etl.transform import (
    transform_alunos,
    transform_resultados,
    transform_questoes
)

from etl.load import (
    load_dataframe
)

def limpar_tabelas():

    conn = duckdb.connect(
        str(DATABASE_PATH)
    )

    conn.execute(
        "DELETE FROM alunos"
    )

    conn.execute(
        "DELETE FROM resultados_alunos"
    )

    conn.execute(
        "DELETE FROM questoes"
    )

    conn.close()

def obter_ano_escolar(nome_turma):

    if nome_turma.startswith("1"):
        return "1"

    if nome_turma.startswith("2"):
        return "2"

    if nome_turma.startswith("3"):
        return "3"

    return "N/A"

def processar_turma(turma_dir):

    turma = turma_dir.name

    ano_escolar = obter_ano_escolar(
        turma
    )

    for arquivo in turma_dir.glob(
        "*.xlsx"
    ):

        bimestre = int(
            arquivo.name[0]
        )

        nome = arquivo.stem

        if nome.endswith("BR"):

            df = read_br(
                arquivo
            )

            alunos = transform_alunos(
                df,
                turma,
                ano_escolar
            )
            todos_alunos.append(alunos)

            resultados = transform_resultados(
                df,
                turma,
                ano_escolar,
                bimestre
            )

            #load_dataframe(
            #    alunos,
            #    "alunos"
            #)

            load_dataframe(
                resultados,
                "resultados_alunos"
            )

        elif nome.endswith("BQ"):

            df = read_bq(
                arquivo
            )

            questoes = transform_questoes(
                df,
                turma,
                ano_escolar,
                bimestre
            )

            load_dataframe(
                questoes,
                "questoes"
            )

def main():

    create_database()

    limpar_tabelas()

    for turma_dir in RAW_DATA_DIR.iterdir():

        if turma_dir.is_dir():

            processar_turma(
                turma_dir
            )

    alunos_df = pd.concat(
    todos_alunos,
    ignore_index=True
    )

    alunos_df = alunos_df.drop_duplicates(
    subset=["matricula"]
    )

    load_dataframe(
        alunos_df,
        "alunos"
    )

    conn = duckdb.connect(
    str(DATABASE_PATH)
    )

    alunos = conn.execute("""
        SELECT COUNT(*)
        FROM alunos
    """).fetchone()[0]

    resultados = conn.execute("""
        SELECT COUNT(*)
        FROM resultados_alunos
    """).fetchone()[0]

    questoes = conn.execute("""
        SELECT COUNT(*)
        FROM questoes
    """).fetchone()[0]

    print("\n===== AUDITORIA =====")

    print(f"Alunos: {alunos}")
    print(f"Resultados: {resultados}")
    print(f"Questões: {questoes}")

    print("=====================\n")

    conn.close()
    
    print(
        "ETL concluído."
    )


if __name__ == "__main__":
    main()
