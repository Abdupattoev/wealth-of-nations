from src.data_io import load_indicator
from src.config import INDICATORS

def main():
    gdp = load_indicator(INDICATORS["gdp_per_capita"])
    print(gdp.head())
    print("\nRows:", len(gdp))

if __name__ == "__main__":
    main()

