import pandas as pd
from src.config import ID_COL

def load_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df[ID_COL] = df[ID_COL].astype(str).str.strip()
    df[ID_COL] = df[ID_COL].str.replace(r"\s+", " ", regex=True)
    return df
