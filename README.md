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
conda create -n wealth_env python=3.13
conda activate wealth_env
```


### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Analysis Script (Optional)

```bash
python main.py
```

### 5. Launch the Streamlit Web App

```bash
streamlit run app.py
```

Then open the browser URL shown in your terminal to interact with the dashboard.

### 🗂️ Project Structure

wealth_of_nations/

│

├── README.md              ← Project overview and setup instructions

├── requirements.txt       ← List of required Python packages

├── main.py                ← Main script for data analysis (optional)

├── app.py                 ← Streamlit application (web dashboard)

│
├── src/                   ← Source code folder

│   ├── __init__.py

│   ├── data_loader.py     ← Functions to load World Bank data using wbgapi

│   ├── data_processing.py ← Functions for cleaning and reshaping data

│   ├── analysis.py        ← Functions for analysis (correlations, trends)

│   └── visualization.py   ← Functions for charts using matplotlib/seaborn

│

└── data/                  ← (Optional) Folder for downloaded or exported datasets

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

