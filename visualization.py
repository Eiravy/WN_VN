import streamlit as st      # Streamlit for web app
import plotly.express as px     # Plotly Express for plotting
import seaborn as sns       # Seaborn for color palettes
import matplotlib.pyplot as plt     # Matplotlib for setting colors
import matplotlib.colors as mcolors     # Convert colors to hex
import matplotlib.cm as cm      # Colormaps
import pycountry        # For converting country names to ISO codes

def data_visualization(df, end_year, bg_color, text_color, palette, cmap_for_map):
    theme_name=''       # Placeholder for theme selection
    st.header("4. Animated Scatter (GDP vs Life Expectancy)")
    # Create animated scatter plot: GDP vs Life Expectancy
    fig_anim=px.scatter(df,x='GDP_per_Capita',y='Life_Expectancy',animation_frame='Year',
                        animation_group='Country',size='Population',color='Country',hover_name='Country',
                        log_x=True,size_max=45,
                        range_x=[df['GDP_per_Capita'].min()*0.9, df['GDP_per_Capita'].max()*1.1],
                        range_y=[df['Life_Expectancy'].min()-5, df['Life_Expectancy'].max()+5],
                        template='plotly_dark' if theme_name=="Dark" else 'plotly_white')
    st.plotly_chart(fig_anim,use_container_width=True,height=600)

    st.header("5. Choropleth: Life Expectancy Over Time")
    # Function to convert country name to ISO alpha-3 code
    def get_iso3(name):
        manual={"Viet Nam":"VNM","Russian Federation":"RUS"}        # Manual corrections
        if name in manual: return manual[name]
        try: return pycountry.countries.lookup(name).alpha_3
        except: return None
    # Add ISO code column
    df['iso_alpha']=df['Country'].map(get_iso3)
    # Drop rows without ISO code
    df_bdd=df.dropna(subset=['iso_alpha'])
    # Create animated choropleth map
    fig_chor=px.choropleth(df_bdd,locations='iso_alpha',color='Life_Expectancy',
                            hover_name='Country',animation_frame='Year',
                            range_color=[df_bdd['Life_Expectancy'].min(),df_bdd['Life_Expectancy'].max()],
                            color_continuous_scale=cmap_for_map,title="Life Expectancy Over Time")
    # Update layout with theme colors
    fig_chor.update_layout(paper_bgcolor=bg_color,plot_bgcolor=bg_color,font=dict(color=text_color),
                           geo=dict(showframe=False,showcoastlines=True))
    st.plotly_chart(fig_chor,use_container_width=True,height=600)
#----------------------------------------------------------------------------------------------------------
def set_theme(theme_name, n_colors):
    # Map of colormap names
    colormap_map = {"Blues":"Blues","Greens":"Greens","Reds":"Reds",
                    "Cividis":"cividis","Inferno":"inferno","Magma":"magma",
                    "Plasma":"plasma","Rainbow":"rainbow","Turbo":"turbo"}
    # Light theme
    if theme_name=="Light":
        bg="#f0f2f6"; text="#000000"
        sns.set_theme(style="whitegrid")
        palette=[mcolors.to_hex(c) for c in sns.color_palette("tab10", n_colors=n_colors)]
        cmap_for_map="viridis"
    # Dark theme
    elif theme_name=="Dark":
        bg="#0e1117"; text="#ffffff"
        sns.set_theme(style="darkgrid")
        palette=[mcolors.to_hex(c) for c in sns.color_palette("tab10", n_colors=n_colors)]
        cmap_for_map="viridis"
    # Other colormap themes
    else:
        cmap=cm.get_cmap(colormap_map[theme_name])
        palette=[mcolors.to_hex(cmap(i/(n_colors-1))) for i in range(n_colors)]
        bg="#0e1117"; text="#ffffff"
        cmap_for_map=colormap_map[theme_name]
    # Update matplotlib text colors
    plt.rcParams.update({'text.color':text,'axes.labelcolor':text,
                         'xtick.color':text,'ytick.color':text,'axes.titlecolor':text})
    # Update Streamlit background and sidebar colors
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{background-color: {bg}; color: {text};}}
    [data-testid="stSidebar"] {{background-color: {bg}; color: {text};}}
    svg {{ color: {text}; }}
    </style>
    """, unsafe_allow_html=True)
    # Return colors and palette for plots
    return bg, text, palette, cmap_for_map
