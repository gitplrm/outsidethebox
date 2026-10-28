from repository.database import get_connection

def get_anos():

    conn = get_connection()

    df = conn.execute("""
        SELECT DISTINCT ano_escolar
        FROM alunos
        ORDER BY ano_escolar
    """).fetchdf()

    conn.close()

    return df

def get_turmas_por_ano(ano):

    conn = get_connection()

    df = conn.execute("""
        SELECT DISTINCT turma
        FROM alunos
        WHERE ano_escolar = ?
        ORDER BY turma
    """, [ano]).fetchdf()

    conn.close()

    return df

def get_alunos_por_turma(turma):

    conn = get_connection()

    df = conn.execute("""
        SELECT
            matricula,
            nome
        FROM alunos
        WHERE turma = ?
        ORDER BY nome
    """, [turma]).fetchdf()

    conn.close()

    return df

def get_evolucao_aluno(matricula):

    conn = get_connection()

    df = conn.execute("""
        SELECT
            bimestre,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM resultados_alunos
        WHERE matricula = ?
        GROUP BY bimestre
        ORDER BY bimestre
    """, [matricula]).fetchdf()

    conn.close()

    return df

def get_evolucao_disciplinas(matricula):

    conn = get_connection()

    df = conn.execute("""
        SELECT
            disciplina,
            bimestre,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM resultados_alunos
        WHERE matricula = ?
        GROUP BY disciplina, bimestre
        ORDER BY disciplina, bimestre
    """, [matricula]).fetchdf()

    conn.close()

    return df

def get_resumo_aluno(matricula):

    conn = get_connection()

    df = conn.execute("""
        SELECT
            disciplina,
            ROUND(
                AVG(percentual_acerto) * 100,
                2
            ) AS media
        FROM resultados_alunos
        WHERE matricula = ?
        GROUP BY disciplina
        ORDER BY media DESC
    """, [matricula]).fetchdf()

    conn.close()

    return df

def get_ranking_turma(turma):

    conn = get_connection()

    df = conn.execute("""
        SELECT
            a.nome,
            ROUND(
                AVG(
                    r.percentual_acerto
                ) * 100,
                2
            ) AS media
        FROM resultados_alunos r
        INNER JOIN alunos a
            ON a.matricula = r.matricula
        WHERE a.turma = ?
        GROUP BY a.nome
        ORDER BY media DESC
    """, [turma]).fetchdf()

    conn.close()

    return df

