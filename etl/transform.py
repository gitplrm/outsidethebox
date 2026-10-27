import pandas as pd


DISCIPLINAS_BR = [
    "MAT",
    "PORT",
    "ING",
    "HIST",
    "GEO",
    "FILO",
    "SOC",
    "BIO",
    "FÍS",
    "QUI",
    "FIN"
]
def transform_alunos(
    df: pd.DataFrame,
    turma: str,
    ano_escolar: str
) -> pd.DataFrame:

    alunos = df[[
        "NR RA",
        "Nome"
    ]].copy()

    alunos.columns = [
        "matricula",
        "nome"
    ]

    alunos["ano_escolar"] = ano_escolar
    alunos["turma"] = turma
    alunos["status"] = "Ativo"

    return alunos[
        [
            "ano_escolar",
            "turma",
            "matricula",
            "nome",
            "status"
        ]
    ]
def transform_resultados(
    df: pd.DataFrame,
    turma: str,
    ano_escolar: str,
    bimestre: int
) -> pd.DataFrame:

    melted = df.melt(
        id_vars=["NR RA", "Nome"],
        value_vars=[
            c for c in DISCIPLINAS_BR
            if c in df.columns
        ],
        var_name="disciplina",
        value_name="percentual_acerto"
    )
    
    melted = melted.dropna(
        subset=["percentual_acerto"]
    )

    melted.rename(
        columns={
            "NR RA": "matricula"
        },
        inplace=True
    )

    melted["ano_escolar"] = ano_escolar
    melted["turma"] = turma
    melted["bimestre"] = bimestre

    return melted[
        [
            "ano_escolar",
            "turma",
            "bimestre",
            "matricula",
            "disciplina",
            "percentual_acerto"
        ]
    ]
def transform_questoes(
    df: pd.DataFrame,
    turma: str,
    ano_escolar: str,
    bimestre: int
) -> pd.DataFrame:

    questoes = df.copy()

    questoes.rename(
        columns={
            "(%) Acertos": "percentual_acerto",
            "Descritor": "descritor",
            "Disciplina": "disciplina",
            "Aula": "aula_url"
        },
        inplace=True
    )

    questoes["ano_escolar"] = ano_escolar
    questoes["turma"] = turma
    questoes["bimestre"] = bimestre

    return questoes[
        [
            "ano_escolar",
            "turma",
            "bimestre",
            "disciplina",
            "descritor",
            "percentual_acerto",
            "aula_url"
        ]
    ]

