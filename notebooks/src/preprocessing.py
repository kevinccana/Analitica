import numpy as np
import pandas as pd

LATE_COLS = [
    "NumberOfTime30-59DaysPastDueNotWorse",
    "NumberOfTimes90DaysLate",
    "NumberOfTime60-89DaysPastDueNotWorse",
]
WINSORIZE_COLS = ["RevolvingUtilizationOfUnsecuredLines", "DebtRatio"]


def fit_preprocessing(df: pd.DataFrame) -> dict:
    """Calcula los parámetros de limpieza (medianas, cotas de winsorización)
    a partir de `df`. Debe ajustarse solo con datos de entrenamiento para
    evitar fuga de información hacia validación/prueba."""
    error_mask = (df[LATE_COLS] >= 96).any(axis=1)
    age_valid = df.loc[df["age"] > 0, "age"]

    return {
        "median_age": age_valid.median(),
        "median_income": df["MonthlyIncome"].median(),
        "median_dependents": df["NumberOfDependents"].median(),
        "late_col_medians": {c: df.loc[~error_mask, c].median() for c in LATE_COLS},
        "winsor_bounds": {
            c: (df[c].quantile(0.01), df[c].quantile(0.99)) for c in WINSORIZE_COLS
        },
    }


def apply_preprocessing(df: pd.DataFrame, bounds: dict) -> pd.DataFrame:
    """Aplica la limpieza documentada en docs/diccionario_datos.md (hallazgos
    de P1) usando los parámetros de `bounds` (ver fit_preprocessing)."""
    df = df.copy()

    error_mask = (df[LATE_COLS] >= 96).any(axis=1)
    df["flag_codigo_error"] = error_mask.astype(int)
    for c in LATE_COLS:
        df.loc[df[c] >= 96, c] = np.nan
        df[c] = df[c].fillna(bounds["late_col_medians"][c])

    df["flag_income_imputado"] = df["MonthlyIncome"].isna().astype(int)
    df["MonthlyIncome"] = df["MonthlyIncome"].fillna(bounds["median_income"])

    df["NumberOfDependents"] = df["NumberOfDependents"].fillna(
        bounds["median_dependents"]
    )

    df.loc[df["age"] == 0, "age"] = np.nan
    df["age"] = df["age"].fillna(bounds["median_age"])

    for c in WINSORIZE_COLS:
        lo, hi = bounds["winsor_bounds"][c]
        df[c] = df[c].clip(lower=lo, upper=hi)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Conveniencia para uso descriptivo (P2): ajusta y aplica sobre el
    mismo conjunto. No usar este atajo para el modelo predictivo (P3): ahí
    se debe ajustar con `fit_preprocessing` solo sobre el train split."""
    bounds = fit_preprocessing(df)
    return apply_preprocessing(df, bounds)
