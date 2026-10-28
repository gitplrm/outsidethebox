from repository.database import get_connection

def get_anos_questoes():

    conn = get_connection()

    df = conn.execute("""
        SELECT DISTINCT ano_escolar
        FROM questoes
        ORDER BY ano_escolar
    """).fetchdf()

    conn.close()

    return df

def get_disciplinas():

    conn = get_connection()

    df = conn.execute("""
        SELECT DISTINCT disciplina
        FROM questoes
        ORDER BY disciplina
    """).fetchdf()

    conn.close()

    return df

def get_turmas_por_ano(ano):

    conn = get_connection()

    df = conn.execute("""
        SELECT DISTINCT turma
        FROM questoes
        WHERE ano_escolar = ?
        ORDER BY turma
    """, [ano]).fetchdf()

    conn.close()

    return df

def get_questoes_ano(
    ano,
    disciplina
):

    conn = get_connection()

    df = conn.execute("""
        SELECT
            descritor,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS percentual_acerto,
            MAX(aula_url) AS aula_url
        FROM questoes
        WHERE ano_escolar = ?
          AND disciplina = ?
        GROUP BY descritor
        ORDER BY percentual_acerto
    """,
    [ano, disciplina]
    ).fetchdf()

    conn.close()

    return df

def get_questoes_turma(
    ano,
    turma,
    disciplina
):

    conn = get_connection()

    df = conn.execute("""
        SELECT
            descritor,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS percentual_acerto,
            MAX(aula_url) AS aula_url
        FROM questoes
        WHERE ano_escolar = ?
          AND turma = ?
          AND disciplina = ?
        GROUP BY descritor
        ORDER BY percentual_acerto
    """,
    [ano, turma, disciplina]
    ).fetchdf()

    conn.close()

    return df

def get_questoes_dificeis():

    conn = get_connection()

    df = conn.execute("""
        SELECT
            disciplina,
            descritor,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM questoes
        GROUP BY disciplina, descritor
        ORDER BY media ASC
        LIMIT 20
    """).fetchdf()

    conn.close()

    return df

def get_questoes_faceis():

    conn = get_connection()

    df = conn.execute("""
        SELECT
            disciplina,
            descritor,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM questoes
        GROUP BY disciplina, descritor
        ORDER BY media DESC
        LIMIT 20
    """).fetchdf()

    conn.close()

    return df

def get_ranking_descritores():

    conn = get_connection()

    df = conn.execute("""
        SELECT
            descritor,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM questoes
        GROUP BY descritor
        ORDER BY media ASC
    """).fetchdf()

    conn.close()

    return df

def get_disciplinas_por_ano(ano):

    conn = get_connection()

    df = conn.execute("""
        SELECT DISTINCT disciplina
        FROM questoes
        WHERE ano_escolar = ?
        ORDER BY disciplina
    """, [ano]).fetchdf()

    conn.close()

    return df

def get_disciplinas_por_ano(ano):

    conn = get_connection()

    df = conn.execute("""
        SELECT DISTINCT disciplina
        FROM questoes
        WHERE ano_escolar = ?
        ORDER BY disciplina
    """, [ano]).fetchdf()

    conn.close()

    return df