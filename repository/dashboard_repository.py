from repository.database import get_connection


def get_kpis():

    conn = get_connection()

    query = """
        SELECT
            (SELECT COUNT(*) FROM alunos) alunos,
            (SELECT COUNT(*) FROM questoes) questoes,
            (SELECT COUNT(DISTINCT turma)
             FROM alunos) turmas
    """

    df = conn.execute(query).fetchdf()

    conn.close()

    return df.iloc[0]