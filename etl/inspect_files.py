from pathlib import Path
import pandas as pd

from config.settings import RAW_DATA_DIR


def inspect_files():

    for turma_dir in RAW_DATA_DIR.iterdir():

        if not turma_dir.is_dir():
            continue

        print(f"\n===== TURMA {turma_dir.name} =====")

        for arquivo in turma_dir.glob("*.xlsx"):

            print(f"\nArquivo: {arquivo.name}")

            df = pd.read_excel(arquivo)

            print(df.columns.tolist())


if __name__ == "__main__":
    inspect_files()