import pandas as pd

from src.config import RAW_TRAINING_FILE


def load_raw_training() -> pd.DataFrame:
    df = pd.read_csv(RAW_TRAINING_FILE, index_col=0)
    return df
