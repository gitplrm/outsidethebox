from pathlib import Path
import pandas as pd


def read_br(filepath: Path) -> pd.DataFrame:

    return pd.read_excel(
        filepath,
        header=2
    )


def read_bq(filepath: Path) -> pd.DataFrame:

    return pd.read_excel(
        filepath,
        header=2
    )