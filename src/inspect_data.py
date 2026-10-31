from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw/Sample - Superstore.csv")

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset tidak ditemukan: {DATA_PATH}")

df = pd.read_csv(DATA_PATH, encoding="latin1")

print(f"Shape: {df.shape[0]} rows, {df.shape[1]} cols\n")

print("Columns:")
print(df.columns.tolist())

print("\nSample records:")
print(df.head().to_string(index=False))

print("\nData Types:")
print(df.dtypes)

print("\nMissing values count:")
print(df.isnull().sum())

print(f"\nDuplicates: {df.duplicated().sum()}")