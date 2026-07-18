from pathlib import Path

SEED = 42

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PROJECT_ROOT / "datos" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "datos" / "processed"
DATA_EXTERNAL = PROJECT_ROOT / "datos" / "external"
MODELS_DIR = PROJECT_ROOT / "notebooks" / "models"
FIGURES_DIR = PROJECT_ROOT / "notebooks" / "figures"
POWERBI_DIR = PROJECT_ROOT / "powerbi"

RAW_TRAINING_FILE = DATA_RAW / "cs-training.csv"
TARGET_COL = "SeriousDlqin2yrs"

MLFLOW_TRACKING_URI = f"sqlite:///{(PROJECT_ROOT / 'mlflow.db').as_posix()}"
