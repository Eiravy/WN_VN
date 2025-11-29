import streamlit as st      # Streamlit for web app
import plotly.express as px     # Plotly Express for plotting
import seaborn as sns       # Seaborn for color palettes
import matplotlib.pyplot as plt     # Matplotlib for setting colors
import matplotlib.colors as mcolors     # Convert colors to hex
import matplotlib.cm as cm      # Colormaps

# --------------------------------------------------
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

# --------------------------------------------------

def data_visualization(df, end_year, bg_color, text_color, palette, cmap_for_map):
    theme_name=''       # Placeholder for theme selection
    st.header("4. Animated Scatter (GDP vs Life Expectancy)")
    # Create animated scatter plot: GDP vs Life Expectancy
    fig_anim=px.scatter(df,x='GDP_per_Capita',y='Life_Expectancy',animation_frame='Year',
                        animation_group='Country',size='Population',color='Country',hover_name='Country',
                        log_x=True,size_max=45,
                        range_x=[df['GDP_per_Capita'].min()*0.9, df['GDP_per_Capita'].max()*1.1],
                        range_y=[df['Life_Expectancy'].min()-5, df['Life_Expectancy'].max()+5],
                        template='plotly_dark' if theme_name=="Dark" else 'plotly_white',
                        color_discrete_sequence=palette)
    # set height in layout
    fig_anim.update_layout(height=600)
    # Show chart
    st.plotly_chart(fig_anim, use_container_width=True, config={"responsive": True})
