"""
Task #1: Acquire and load Kickstarter dataset
-----------------------------------------------
Loads and performs an initial inspection of the Kickstarter Projects
dataset for the crowdfunding recommendation engine project.
"""

import pandas as pd
import numpy as np
import os

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 150)


# =============================================================================
# STEP 1 — LOAD THE DATASET
# =============================================================================
DATA_PATH = "data/DSI_kickstarterscrape_dataset.csv"

def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Could not find '{path}'. Unzip the dataset into the data/ "
            f"folder first, then update DATA_PATH if your filename differs."
        )
    df = pd.read_csv(path, encoding="latin1")
    print(f"Loaded '{path}' successfully.")
    return df


# =============================================================================
# STEP 2 — INITIAL INSPECTION
# =============================================================================
def inspect_data(df: pd.DataFrame) -> None:
    print("\n" + "=" * 70)
    print("SHAPE")
    print("=" * 70)
    print(f"Rows: {df.shape[0]:,}  |  Columns: {df.shape[1]}")

    print("\n" + "=" * 70)
    print("COLUMN NAMES")
    print("=" * 70)
    for col in df.columns:
        print(f"  - {col}")

    print("\n" + "=" * 70)
    print("DATA TYPES")
    print("=" * 70)
    print(df.dtypes)

    print("\n" + "=" * 70)
    print("FIRST 5 ROWS")
    print("=" * 70)
    print(df.head())

    print("\n" + "=" * 70)
    print("MISSING VALUES (count and %)")
    print("=" * 70)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    missing_summary = pd.DataFrame({"missing_count": missing, "missing_pct": missing_pct})
    print(missing_summary[missing_summary["missing_count"] > 0].sort_values(
        "missing_count", ascending=False
    ))
    if missing_summary["missing_count"].sum() == 0:
        print("No missing values found.")

    print("\n" + "=" * 70)
    print("DUPLICATE ROWS")
    print("=" * 70)
    print(f"Fully duplicated rows: {df.duplicated().sum()}")
    if "project id" in df.columns:
        print(f"Duplicate project ids: {df['project id'].duplicated().sum()}")

    print("\n" + "=" * 70)
    print("STATUS VALUE COUNTS")
    print("=" * 70)
    status_col_candidates = [c for c in df.columns if c.lower() in ("state", "status")]
    if status_col_candidates:
        col = status_col_candidates[0]
        print(df[col].value_counts(dropna=False))
    else:
        print("No 'state'/'status' column detected — check column names above.")

    print("\n" + "=" * 70)
    print("CATEGORY VALUE COUNTS")
    print("=" * 70)
    if "category" in df.columns:
        print(df["category"].value_counts(dropna=False))

    print("\n" + "=" * 70)
    print("NUMERIC SUMMARY STATISTICS")
    print("=" * 70)
    print(df.describe(include=[np.number]))

    print("\n" + "=" * 70)
    print("CATEGORICAL / OBJECT COLUMN CARDINALITY")
    print("=" * 70)
    obj_cols = df.select_dtypes(include="object").columns
    for col in obj_cols:
        print(f"  - {col}: {df[col].nunique()} unique values")


if __name__ == "__main__":
    df = load_data()
    inspect_data(df)