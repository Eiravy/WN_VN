# 🌍 Wealth of Nations

This project explores the relationship between **GDP per capita** and **life expectancy** across nations using **World Bank Open Data**. It provides both data analysis and an interactive dashboard built with **Streamlit**.

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

### 📈 What You Can Do with This Project
Compare GDP and life expectancy across countries and regions

Visualize historical trends with line plots

Explore correlations and data insights interactively

Extend the analysis with new indicators (e.g., education, health spending)

### 🧪 Skills Demonstrated

✅ Git & GitHub

✅ Data Wrangling with pandas

✅ World Bank API integration using wbgapi

✅ Data Visualization (matplotlib & seaborn)

✅ Building interactive dashboards with Streamlit

✅ Project structuring and modular code design


### 💡 Ideas for Extension

Add more indicators (e.g., education, CO2 emissions)

Build regional comparisons or economic clusters

Deploy the Streamlit app online (e.g., via Streamlit Cloud or Hugging Face Spaces)

### 📬 Contact

Le Hong Vy Ngoc

Master Student, Università degli Studi di Milano Statale

Major: Data Science for Health and Economics

📧 hongvyngoc.le@studenti.unimi.it
📧 vyngoc100@gmail.com

