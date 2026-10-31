import pandas as pd
from pathlib import Path


def extract_data():
    """
    Extract raw sales data from CSV.
    """
    file_path = Path("data/raw/Sample - Superstore.csv")

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    print("Starting data extraction...")

    # Read CSV
    df = pd.read_csv(
        file_path,
        encoding="latin1"
    )

    print("Extraction completed!")
    print(f"Total records extracted: {len(df)}")

    return df


if __name__ == "__main__":
    data = extract_data()

    print("\nExtracted data preview:")
    print(data.head())
