import pandas as pd
from pathlib import Path
from src.config import RAW_DIR

def load_raw(name: str) -> pd.DataFrame:
    """
    Loads the raw downloaded file from data/raw.
    Returns it exactly as stored (wide format).
    """
    file_path = RAW_DIR / f"{name}.csv"
    return pd.read_csv(file_path)
