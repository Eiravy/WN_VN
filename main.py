import streamlit as st
import wbgapi as wb
from data_loader import data_loader
from data_analysis import data_analysis
from visualization import data_visualization, set_theme
from ml_prediction import machinelearning_clustering

# Page config
st.set_page_config(page_title="Wealth of Nations Dashboard", page_icon="🌍", layout="wide")
col1, col2 = st.columns([3, 1])  # 3:1 ratio
with col1:
    st.title("Quantitative analysis of global socio-economic indicators: examining GDP per capita, life expectancy, population, and school enrollment across nations to reveal developmental trends, correlations, and patterns using World Bank Open Data.")
    st.write("Data source: World Bank Open Data API - wbgapi - https://pypi.org/project/wbgapi/")

with col2:
    st.image("./figure/VN.JPG", width=300)  # adjust width as needed
    st.markdown("""
    <div style='text-align: left; line-height:2.5;'>
    Le Hong Vy Ngoc  <br>
    <a href='https://eiravy.github.io/' target='_blank'>https://eiravy.github.io/</a> <br>
    email: hongvyngoc.le@studenti.unimi.it  <br>    
    </div>
    """, unsafe_allow_html=True)
    st.image("./figure/logo.png", width=300)  # adjust width as needed
all_countries = wb.economy.DataFrame()
country_names = all_countries['name'].tolist()
st.sidebar.header("Filter Options")
selected_countries = st.sidebar.multiselect("Select countries:", options=country_names,
                                            default=["United States","China","India","Germany","Italy",
                                                     "Russian Federation","Poland","France","Austria",
                                                     "Finland","Malaysia","Japan","Viet Nam","Thailand"])
start_year = st.sidebar.slider("Start year", 1980, 2020, 1980)
end_year = st.sidebar.slider("End year", 1980, 2020, 2020)
economies = wb.economy.DataFrame()
selected_codes = [code for code,name in zip(economies.index,economies['name']) if name in selected_countries]
theme_name = st.sidebar.selectbox("Select Theme / Palette",
                                  ["Light","Dark"])

bg_color, text_color, palette, cmap_for_map = set_theme(theme_name, max(1,len(selected_countries)))
# 1️⃣ Data Loader
df = data_loader(selected_codes, start_year, end_year)
# 2️⃣ Data Analysis
data_analysis(df, theme_name, palette)
# 3️⃣ Data Visualization
data_visualization(df, end_year, bg_color, text_color, palette, cmap_for_map)
# 4️⃣ Machine Learning & Clustering
machinelearning_clustering(df, selected_countries, end_year)
