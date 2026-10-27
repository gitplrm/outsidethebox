# Outside The Box

Dashboard educacional para análise de desempenho de estudantes do Ensino Médio utilizando Python, DuckDB, Pandas, Streamlit e Plotly.

## Objetivo

O projeto tem como objetivo transformar planilhas de resultados bimestrais em uma plataforma analítica que permita acompanhar:

- desempenho geral das turmas;
- desempenho por disciplina;
- evolução dos estudantes ao longo dos bimestres;
- ranking de turmas;
- ranking de estudantes;
- descritores com maior dificuldade;
- questões com maiores e menores índices de acerto.

Toda a solução foi construída utilizando ferramentas open-source.

---

# Tecnologias

- Python
- Pandas
- DuckDB
- Streamlit
- Plotly
- OpenPyXL

---

# Arquitetura

```text
Planilhas Excel
        ↓
    ETL Pandas
        ↓
      DuckDB
        ↓
   Repository SQL
        ↓
 Dashboard Streamlit
```

O sistema segue arquitetura em camadas:

```text
├── Ingestão de Dados
├── Transformação (ETL)
├── Persistência (DuckDB)
├── Camada de Consultas
└── Interface (Streamlit)
```

---

# Estrutura do Projeto

```text
outsidethebox_v_1.0/

├── config/
│   ├── __init__.py
│   └── settings.py
│
├── data/
│   ├── raw/
│   └── database/
│
├── dashboard/
│   ├── app.py
│   └── pages/
│
├── etl/
│   ├── create_database.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── run_etl.py
│   └── audit.py
│
├── repository/
│   ├── database.py
│   ├── dashboard_repository.py
│   └── turma_repository.py
│
├── requirements.txt
└── README.md
```

---

# Organização dos Dados

Os dados devem ser organizados em pastas por turma.

Exemplo:

```text
data/raw/

├── 1A/
│   ├── 1BR.xlsx
│   ├── 1BQ.xlsx
│   ├── 2BR.xlsx
│   ├── 2BQ.xlsx
│   ├── 3BR.xlsx
│   └── 3BQ.xlsx
│
├── 1B/
├── 1C/
├── 2B/
├── 2Enf/
└── 3B/
```

Onde:

```text
BR = Resultados dos alunos
BQ = Resultados das questões
```

---

# Instalação

## 1. Clonar projeto

```bash
git clone <URL_DO_REPOSITORIO>

cd outsidethebox_v_1.0
```

---

## 2. Criar ambiente virtual

Linux:

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Construção da Base

O banco DuckDB é criado automaticamente.

Executar:

```bash
python -m etl.run_etl
```

Ao final será criado:

```text
data/database/educacao.duckdb
```

---

# Atualização dos Dados

Sempre que novas planilhas forem adicionadas ou substituídas:

```bash
python -m etl.run_etl
```

O processo:

1. limpa as tabelas analíticas;
2. relê todas as planilhas;
3. reconstrói a base de dados.

Não é necessário executar scripts SQL manualmente.

---

# Estrutura Analítica

## ALUNOS

```text
ano_escolar
turma
matricula
nome
status
```

---

## RESULTADOS_ALUNOS

```text
ano_escolar
turma
bimestre
matricula
disciplina
percentual_acerto
```

---

## QUESTOES

```text
ano_escolar
turma
bimestre
disciplina
descritor
percentual_acerto
aula_url
```

---

# Executando o Dashboard

Na raiz do projeto:

```bash
PYTHONPATH=. streamlit run dashboard/app.py
```

Acesse:

```text
http://localhost:8501
```

---

# Funcionalidades Implementadas

## Indicadores

- Média geral por turma
- Média por disciplina
- Ranking de turmas

## Banco Analítico

- DuckDB persistente
- Reprocessamento automático
- ETL em Pandas

## Dashboard

- Streamlit
- Plotly
- Tabelas ordenáveis

---

# Roadmap

## Próximas Implementações

### Página Alunos

- Evolução por bimestre
- Evolução por disciplina
- Comparação com turma
- Ranking individual

### Página Questões

- Filtro por série
- Filtro por disciplina
- Filtro por turma
- Questões mais difíceis
- Questões mais fáceis
- Ranking de descritores
- Links diretos para aulas

### Melhorias Técnicas

- Testes automatizados
- Logs de execução
- Exportação CSV
- Exportação PDF
- Deploy em servidor Linux

---

# Licença

Projeto desenvolvido para fins educacionais e de análise de desempenho escolar.

Todos os dados utilizados pertencem às respectivas instituições responsáveis.
