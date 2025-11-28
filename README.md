# 🌍 Wealth of Nations

Quantitative analysis of global socio-economic indicators: examining **GDP per capita, life expectancy, population, and school enrollment** across nations to reveal developmental trends, correlations, and patterns using World Bank Open Data.

---

## 🔧 Project Setup Instructions

Follow these steps to set up and run the project in a clean Conda environment:

### 1. Clone the Repository

```bash

git clone https://github.com/eiravy/WN_VN

cd WN_VN

```

### 2. Create and Activate a New Conda Environment

```bash 
conda create -n myenv python=3.10.16
conda activate myenv
```

### 3. Launch the Streamlit Web App

```bash
streamlit run main.py
```

Then open the browser URL shown in your terminal to interact with the dashboard.

### 🗂️ Project Structure

WN_VN/

│

├── __init__.py

├── main.py            ← Main script for data analysis (optional)

├── data_loader.py     ← Functions to load World Bank data using wbgapi

├── data_analysis.py   ← Functions for analysis (correlations, trends)

├── visualization.py   ← Functions for charts using matplotlib/seaborn

├── ml_prediction.py   ← Training and testing Linear regression, Random Forest, Decision Tree, K-Means Clustering

└── figure/            ← (Optional) Author's photo

├── README.md          ← Project overview and setup instructions


### 📊 Data Source

All data is retrieved live from the World Bank Open Data API using the wbgapi Python package.

Key indicators used:

GDP per capita (NY.GDP.PCAP.CD)

Life expectancy (SP.DYN.LE00.IN)

Population (SP.POP.TOTL)

School_Enrollment (SE.SEC.ENRR)

### 📈 What You Can Do with This Project
Displays a table with key indicators (GDP_per_Capita, Life_Expectancy, Population, School_Enrollment) for each country and year.

Allows the user to select a metric (GDP, Life Expectancy, Population, or School Enrollment) and visualizes its trend over time using a line chart.

Displays scatter plots showing the relationship between GDP per Capita and other indicators (Life Expectancy, Population, School Enrollment).

This experiment changes K in clustering to group countries by GDP, analyzing how cluster assignments and patterns vary with different K values.

This project trains and tests Life Expectancy using Linear Regression, Decision Tree, and Random Forest, evaluating performance with MAE.

### 🧪 Skills Demonstrated

✅ Git & GitHub

✅ Data Wrangling with pandas

✅ World Bank API integration using wbgapi

✅ Data Visualization (plotly, matplotlib & seaborn)

✅ Building interactive dashboards with Streamlit

✅ Project structuring and modular code design

### 📬 Contact

Le Hong Vy Ngoc

Master Student, Università degli Studi di Milano Statale

Major: Data Science for Health and Economics

📧 hongvyngoc.le@studenti.unimi.it
📧 vyngoc100@gmail.com

