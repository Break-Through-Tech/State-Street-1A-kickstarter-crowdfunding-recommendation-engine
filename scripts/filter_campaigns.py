import pandas as pd
from load_and_inspect_data import load_data

df = load_data()

print("Status values before filtering:")
print(df['status'].value_counts(dropna=False))
print(f'\nTotal rows before filtering: {len(df):,}')

df_filtered = df[df["status"].isin(["successful", "failed"])]

print("\nStatus values after filtering:")
print(df_filtered["status"].value_counts(dropna=False))
print(f"\nTotal rows after filtering: {len(df_filtered):,}")
print(f"Rows removed: {len(df) - len(df_filtered):,}")

output_path = "data/kickstarter_filtered.csv"
df_filtered.to_csv(output_path, index=False)
print(f"\nSaved filtered dataset to '{output_path}'")
