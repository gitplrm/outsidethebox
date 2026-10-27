from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = ROOT_DIR / "data" / "raw"

DATABASE_PATH = (
    ROOT_DIR
    / "data"
    / "database"
    / "educacao.duckdb"
)