from pathlib import Path

# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data folders
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# World Bank indicators used in the project
INDICATORS = {
    "gdp_per_capita": "NY.GDP.PCAP.CD",
    "life_expectancy": "SP.DYN.LE00.IN",
    "infant_mortality": "SP.DYN.IMRT.IN",
    "health_spending": "SH.XPD.CHEX.PC.CD",
    "smoking_rate": "SH.PRV.SMOK",
    "birth_rate": "SP.DYN.CBRT.IN",
}

