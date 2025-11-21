import pandas as pd
from pathlib import Path
from src.config import RAW_DIR, PROCESSED_DIR, INDICATORS
from src.data_io import load_raw


def reshape_wide_to_long(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts a wide WB format (YR1990, YR1991...) into long format:
    country | year | value
    """
    df_long = df.melt(
        id_vars=["country"],
        var_name="year",
        value_name="value"
    )

    # Convert "YR1990" -> 1990 (int)
    df_long["year"] = df_long["year"].str.replace("YR", "").astype(int)
    return df_long


def merge_all_raw_indicators() -> pd.DataFrame:
    merged = pd.DataFrame()

    for name in INDICATORS.keys():
        print(f"Processing {name}...")

        # Load raw CSV
        df_raw = load_raw(name)

        # Convert to long form
        df_long = reshape_wide_to_long(df_raw)
        df_long = df_long.rename(columns={"value": name})

        # First indicator initializes merged table
        if merged.empty:
            merged = df_long
        else:
            merged = merged.merge(df_long, on=["country", "year"], how="outer")

    return merged


def main():
    print("Processing data...")

    merged = merge_all_raw_indicators()

    # Save final processed dataset
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    merged.to_csv(PROCESSED_DIR / "world_bank_processed.csv", index=False)

    print("✔ Processing complete!")
    print("✔ Saved:", PROCESSED_DIR / "world_bank_processed.csv")


if __name__ == "__main__":
    main()




