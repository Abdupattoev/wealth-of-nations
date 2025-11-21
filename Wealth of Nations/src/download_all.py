from src.config import INDICATORS
from src.data_io import load_indicator, save_raw
from src.config import RAW_DIR


def main():
    print("Starting download...\n")

    for name, code in INDICATORS.items():
        print(f"→ Downloading {name} ({code}) ...")
        try:
            df = load_indicator(code)
        except Exception as e:
            print(f"   ⚠ Error downloading {name}: {e}")
            continue

        if df is None or df.empty:
            print(f"   ⚠ No data returned for {name}")
        else:
            save_raw(name, df)
            print(f"   ✓ Saved raw data for {name}")

    print("\nAll downloads complete!")
    print(f"Raw files saved to: {RAW_DIR}")


if __name__ == "__main__":
    main()



