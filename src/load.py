import os
from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)

def load_data(df):
    """
    Load transformed sales data into PostgreSQL.
    """

    print("Starting data loading...")

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    missing_settings = [
        name
        for name, value in (
            ("DB_USER", user),
            ("DB_PASSWORD", password),
            ("DB_HOST", host),
            ("DB_PORT", port),
            ("DB_NAME", database),
        )
        if not value
    ]
    if missing_settings:
        raise ValueError(
            "Database configuration is incomplete. Set: "
            + ", ".join(missing_settings)
        )

    # database connection
    connection_url = (
        f"postgresql+psycopg2://{user}:{password}"
        f"@{host}:{port}/{database}"
    )

    engine = create_engine(connection_url)

    try:
        df.to_sql(
            name="sales_transactions",
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=1000
        )

        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(*) FROM sales_transactions")
            )
            loaded_rows = result.scalar()

        print("Data loading completed!")
        print(f"Source records: {len(df)}")
        print(f"Loaded records: {loaded_rows}")

        if loaded_rows != len(df):
            raise ValueError("Loaded row count does not match source row count")

    finally:
        engine.dispose()


if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    raw_data = extract_data()
    clean_data = transform_data(raw_data)

    load_data(clean_data)
