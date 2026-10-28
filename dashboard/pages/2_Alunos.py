import streamlit as st
import plotly.express as px

from repository.aluno_repository import (
    get_anos,
    get_turmas_por_ano,
    get_alunos_por_turma,
    get_evolucao_aluno,
    get_evolucao_disciplinas,
    get_resumo_aluno,
    get_ranking_turma
)

st.title("👨‍🎓 Alunos")

anos = get_anos()

ano = st.selectbox(
    "Ano Escolar",
    anos["ano_escolar"]
)

turmas = get_turmas_por_ano(ano)

turma = st.selectbox(
    "Turma",
    turmas["turma"]
)

alunos = get_alunos_por_turma(
    turma
)

nome_aluno = st.selectbox(
    "Aluno",
    alunos["nome"]
)

matricula = alunos.loc[
    alunos["nome"] == nome_aluno,
    "matricula"
].iloc[0]

resumo = get_resumo_aluno(
    matricula
)

media_geral = round(
    resumo["media"].mean(),
    2
)

melhor = resumo.iloc[0]

pior = resumo.iloc[-1]

ranking = get_ranking_turma(
    turma
)

posicao = (
    ranking.reset_index()
    .query("nome == @nome_aluno")
    .index[0]
    + 1
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Média Geral",
        f"{media_geral}%"
    )

with col2:
    st.metric(
        "Melhor Disciplina",
        melhor["disciplina"]
    )

with col3:
    st.metric(
        "Pior Disciplina",
        pior["disciplina"]
    )

with col4:
    st.metric(
        "Ranking na Turma",
        f"{posicao}º"
    )

evolucao = get_evolucao_aluno(
    matricula
)

fig = px.line(
    evolucao,
    x="bimestre",
    y="media",
    markers=True,
    title="Evolução Geral"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

disciplinas = get_evolucao_disciplinas(
    matricula
)

fig2 = px.line(
    disciplinas,
    x="bimestre",
    y="media",
    color="disciplina",
    markers=True,
    title="Evolução por Disciplina"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

tabela = disciplinas.pivot_table(
    index="disciplina",
    columns="bimestre",
    values="media"
)

tabela["Média"] = tabela.mean(
    axis=1
)

st.subheader(
    "Desempenho por Disciplina"
)

st.dataframe(
    tabela.round(2),
    use_container_width=True
)

