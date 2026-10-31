
import pandas as pd


def transform_data(df):
    """
    Clean and transform retail sales data.
    """

    print("Starting data transformation...")

    df = df.copy()

    # Standarisasi nama kolom
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[\s-]+", "_", regex=True)
    )

    initial_rows = len(df)

    # hapus data duplikat
    before = len(df)
    df = df.drop_duplicates()
    print("Duplicates removed:", before - len(df))

    # validasi kolom yang diperlukan
    before = len(df)
    df = df.dropna(subset=["order_id", "product_id"])
    print("Rows removed due to missing IDs:", before - len(df))

    # konversi kolom tanggal
    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="coerce"
    )
    df["ship_date"] = pd.to_datetime(
        df["ship_date"], errors="coerce"
    )

    # konversi kolom numerik
    numeric_columns = [
        "sales", "quantity", "discount", "profit"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")


    required_columns = [
        "order_date", "ship_date",
        "sales", "quantity", "discount", "profit"
    ]

    before = len(df)
    df = df.dropna(subset=required_columns)
    print("Rows removed due to invalid values:", before - len(df))

    before = len(df)
    df = df[
        (df["sales"] >= 0) &
        (df["quantity"] > 0)
    ]
    print("Rows removed due to Sales/Quantity rules:", before - len(df))

    df["quantity"] = df["quantity"].astype("int64")

    df["delivery_days"] = (
        df["ship_date"] - df["order_date"]
    ).dt.days

    df["profit_margin"] = (
        df["profit"] / df["sales"] * 100
    ).where(df["sales"] != 0)


    print("\nTRANSFORMATION VALIDATION")

    print("Initial rows:", initial_rows)
    print("Final rows:", len(df))
    print("Total rows removed:", initial_rows - len(df))

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print(
        "\nInvalid date order:",
        (df["ship_date"] < df["order_date"]).sum()
    )

    print(
        "\nNon-positive quantity:",
        (df["quantity"] <= 0).sum()
    )

    print(
        "\nNegative sales:",
        (df["sales"] < 0).sum()
    )

    print("\nTransformation completed!")

    return df


if __name__ == "__main__":
    from extract import extract_data

    raw_data = extract_data()
    clean_data = transform_data(raw_data)

    print("\nClean data preview:")
    print(clean_data.head())
