import pandas as pd

arquivo = "data/raw/1A/3BQ.xlsx"

df = pd.read_excel(
    arquivo,
    header=None
)

print(df.head(20).to_string())