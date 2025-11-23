# 🌍 Wealth of Nations — Data Analysis  
A data-driven project exploring how key socio-economic indicators relate to each other across countries and over time.

This project cleans, merges, analyzes, and visualizes **World Bank** development metrics such as GDP, life expectancy, health spending, smoking rate, infant mortality, and birth rate.

---

## 📁 Project Structure

wealth-of-nations/
│
├── data/
│ ├── raw/ # Raw CSV files (World Bank)
│ └── processed/ # Cleaned merged dataset
│
├── src/
│ ├── config.py # File paths
│ ├── process_data.py # Cleans/merges datasets
│ └── analysis.ipynb # All visualizations & results
│
└── README.md

---

## ⭐ Overview

This project investigates how the following variables relate:

- **GDP per capita**
- **Life expectancy**
- **Infant mortality**
- **Health spending (% of GDP)**
- **Smoking rate (% of adults)**
- **Birth rate (per 1,000 people)**

**Key questions we explore:**

- Do richer countries live longer?
- Does smoking reduce life expectancy?
- Does higher health spending improve national health?
- How does birth rate relate to GDP?

---

## 📊 Dataset Description

Data comes from the **World Bank Open Data API**, cleaned and merged into a single panel dataset.

Each row represents:


Missing values (`NaN`) exist because **not all countries report all indicators every year**.

---

## 🧹 Data Processing

Cleaning steps performed in `process_data.py`:

- Standardized column names  
- Converted years → numeric  
- Removed duplicate entries  
- Merged 6 datasets using (country, year) keys  
- Exported clean dataset:  
  `data/processed/world_bank_processed.csv`

---

## 📈 Visualizations (Examples)

### **1. GDP vs Life Expectancy**
Strong positive relationship — wealthier countries live longer.

### **2. Smoking Rate vs Life Expectancy**
Weak negative relationship — smoking is only a partial factor.

### **3. Health Spending vs Life Expectancy**
Moderate positive correlation — more investment → better outcomes.

### **4. Birth Rate vs GDP per Capita**
Strong negative correlation — richer nations tend to have lower birth rates.

Interactive Plotly versions are included in the notebook.

---

## 📉 Correlation Summary

| Relationship | Correlation |
|-------------|-------------|
| GDP ↔ Life Expectancy | **+0.57** |
| Smoking Rate ↔ Life Expectancy | **−0.18** |
| Smoking Rate ↔ GDP | **+0.01** (very weak) |
| Health Spending ↔ Life Expectancy | **+0.58** |
| Birth Rate ↔ GDP | **−0.49** |

**Insights:**

- Wealth strongly improves life expectancy  
- Smoking has a weaker-than-expected impact globally  
- High-income nations have lower birth rates  
- More health spending generally leads to better outcomes  

---

## ▶️ Running the Project

---

## 🧠 Conclusion

This project demonstrates how development indicators interact across the world:

- **Richer countries enjoy longer lives**
- **Smoking varies widely but correlates only moderately with health**
- **Health investment matters in improving life expectancy**
- **Birth rates drop as nations develop economically**

The dataset and notebook provide a foundation for further machine learning, forecasting, or dashboard creation.

---

## 📎 Data Sources

All indicators downloaded from **The World Bank Open Data Platform**:  
https://data.worldbank.org/

---

## 👨‍💻 Author

**Abdupattoev**  
Student project 
