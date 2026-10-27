from repository.database import (
    get_connection
)
def get_media_por_turma():

    conn = get_connection()

    query = """
        SELECT
            turma,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM resultados_alunos
        GROUP BY turma
        ORDER BY turma
    """

    df = conn.execute(
        query
    ).fetchdf()

    conn.close()

    return df

def get_ranking_turmas():

    conn = get_connection()

    query = """
        SELECT
            turma,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM resultados_alunos
        GROUP BY turma
        ORDER BY media DESC
    """

    df = conn.execute(
        query
    ).fetchdf()

    conn.close()

    return df

def get_media_por_disciplina():

    conn = get_connection()

    query = """
        SELECT
            disciplina,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM resultados_alunos
        GROUP BY disciplina
        ORDER BY media DESC
    """

    df = conn.execute(
        query
    ).fetchdf()

    conn.close()

    return df

