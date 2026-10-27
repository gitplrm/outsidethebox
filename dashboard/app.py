import streamlit as st
import plotly.express as px

from repository.turma_repository import (
    get_media_por_turma,
    get_ranking_turmas,
    get_media_por_disciplina
)

from repository.dashboard_repository import (
    get_kpis
)

st.title("Turmas")

kpis = get_kpis()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Alunos",
        int(kpis["alunos"])
    )

with col2:
    st.metric(
        "Turmas",
        int(kpis["turmas"])
    )

with col3:
    st.metric(
        "Questões",
        int(kpis["questoes"])
    )

media = get_media_por_turma()

st.subheader(
    "Média Geral por Turma"
)

st.dataframe(
    media,
    use_container_width=True
)

ranking = get_ranking_turmas()

fig = px.bar(
    ranking,
    x="turma",
    y="media",
    color="media",
    text="media",
    title="Ranking de Turmas"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

disciplinas = get_media_por_disciplina()

fig2 = px.bar(
    disciplinas,
    x="disciplina",
    y="media",
    color="media",
    text="media",
    title="Média por Disciplina"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)