import streamlit as st  # Streamlit for web app
import wbgapi as wb     # World Bank API
from data_loader import data_loader     # Load World Bank data
from data_analysis import data_analysis     # Analysis functions
from visualization import data_visualization, set_theme     # Visualization functions
from ml_prediction import machinelearning_clustering        # ML & clustering functions

# Page configuration
st.set_page_config(page_title="Wealth of Nations Dashboard", page_icon="🌍", layout="wide")

# Create two columns: main content and sidebar/profile
col1, col2 = st.columns([3, 1])  # 3:1 width ratio

with col1:
    # Title and description
    st.title("Quantitative analysis of global socioeconomic indicators: examining GDP per capita, life expectancy, population, and school enrollment across nations to reveal developmental trends, correlations, and patterns using World Bank Open Data.")
    # Data source info
    st.write("Data source: World Bank Open Data API - wbgapi - https://pypi.org/project/wbgapi/")

with col2:
    # Profile picture / images
    st.image("./figure/VN.JPG", width=300)  # adjust width as needed
    # Author info with link and email
    st.markdown("""
    <div style='text-align: left; line-height:2.5;'>
    Le Hong Vy Ngoc  <br>
    <a href='https://eiravy.github.io/' target='_blank'>https://eiravy.github.io/</a> <br>
    email: hongvyngoc.le@studenti.unimi.it  <br>    
    </div>
    """, unsafe_allow_html=True)
    st.image("./figure/logo.png", width=300)  # adjust width as needed
    
# Get all countries from World Bank
all_countries = wb.economy.DataFrame()
country_names = all_countries['name'].tolist()

# Sidebar filters
st.sidebar.header("Filter Options")
# Multi-select for countries
selected_countries = st.sidebar.multiselect("Select countries:", options=country_names,
                                            default=["United States","China","India","Germany","Italy",
                                                     "Russian Federation","Poland","France","Austria",
                                                     "Finland","Malaysia","Japan","Viet Nam","Thailand"])
# Slider for start and end year
start_year = st.sidebar.slider("Start year", 1980, 2020, 1980)
end_year = st.sidebar.slider("End year", 1980, 2020, 2020)

# Get the codes of selected countries
economies = wb.economy.DataFrame()
selected_codes = [code for code,name in zip(economies.index,economies['name']) if name in selected_countries]

# Theme selection
theme_name = st.sidebar.selectbox("Select Theme / Palette",
                                  ["Light","Dark"])
# Set colors, palette, colormap
bg_color, text_color, palette, cmap_for_map = set_theme(theme_name, max(1,len(selected_countries)))

# Data Loader: load World Bank data for selected countries & years
df = data_loader(selected_codes, start_year, end_year)

# Data Analysis: show tables, trends, correlations
data_analysis(df, theme_name, palette)

# Data Visualization: animated scatter & choropleth maps
data_visualization(df, end_year, bg_color, text_color, palette, cmap_for_map)

# Machine Learning & Clustering: KMeans clusters & life expectancy prediction
machinelearning_clustering(df, selected_countries, end_year)
