import streamlit as st

from repository.questao_repository import (
    get_anos_questoes,
    get_disciplinas_por_ano,
    get_turmas_por_ano,
    get_questoes_ano,
    get_questoes_turma,
    get_questoes_dificeis,
    get_questoes_faceis
)

st.title("📚 Questões")

anos = get_anos_questoes()

ano = st.selectbox(
    "Ano Escolar",
    anos["ano_escolar"]
)

disciplinas = get_disciplinas_por_ano(
    ano
)
disciplina = st.selectbox(
    "Disciplina",
    disciplinas["disciplina"]
)

turmas = get_turmas_por_ano(
    ano
)

opcoes = ["Todas"] + list(
    turmas["turma"]
)

turma = st.selectbox(
    "Turma (opcional)",
    opcoes
)

if turma == "Todas":

    tabela = get_questoes_ano(
        ano,
        disciplina
    )

else:

    tabela = get_questoes_turma(
        ano,
        turma,
        disciplina
    )

st.dataframe(
    tabela,
    use_container_width=True
)

st.subheader(
    "Questões Mais Difíceis"
)

st.dataframe(
    get_questoes_dificeis(),
    use_container_width=True
)

st.subheader(
    "Questões Mais Fáceis"
)

st.dataframe(
    get_questoes_faceis(),
    use_container_width=True
)

