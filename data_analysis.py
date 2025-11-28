import streamlit as st      # Import Streamlit for web app
import plotly.express as px     # Import Plotly Express for easy plots
import plotly.graph_objects as go       # Import Plotly Graph Objects for custom plots
from sklearn.linear_model import LinearRegression       # Import Linear Regression model
import numpy as np      # Import NumPy for numeric operations

def data_analysis(df, theme_name, palette):
    
    st.header("1. Data Table")
    # Show selected columns of data in a table
    st.dataframe(df[['Country','Year','GDP_per_Capita','Life_Expectancy','Population','School_Enrollment']],use_container_width=True,height=500)
    
    st.header("2. Trends Over Time")
    # Select metric to plot
    metrics = ['GDP_per_Capita','Life_Expectancy','Population','School_Enrollment']
    tabs = st.tabs(metrics)
    # Create line chart for selected metric
    for tab, metric in zip(tabs, metrics):
        with tab:
            fig_trend=px.line(df,x='Year',y=metric,color='Country',markers=True,
                      title=f"{metric} Trend Over Time",
                      template='plotly_dark' if theme_name=="Dark" else 'plotly_white')            
            # set height in layout
            fig_trend.update_layout(height=500)
            # Show chart
            st.plotly_chart(fig_trend, use_container_width=True, config={"responsive": True})
    
    
    st.header("3. Correlations")
    indicators = ['Life_Expectancy','Population','School_Enrollment']
    titles = ['Life Expectancy vs GDP','Population vs GDP','School Enrollment vs GDP']
    cols=st.columns(3)      # Create 3 columns for scatter plots
    # Loop through each indicator to create scatter plots with trend line
    for col,y_var,t in zip(cols,indicators,titles):
        # Scatter plot for GDP vs indicator
        fig=px.scatter(df,x='GDP_per_Capita',y=y_var,color='Country',title=t,
                       template='plotly_dark' if theme_name=="Dark" else 'plotly_white',
                       color_discrete_sequence=palette)
        # Remove rows with missing values
        clean=df[['GDP_per_Capita',y_var]].dropna()
        X=clean[['GDP_per_Capita']];     # Predictor
        y=clean[y_var]      # Target
        # Fit linear regression
        model=LinearRegression().fit(X,y)
         # Generate prediction line
        x_range=np.linspace(X.min(),X.max(),100)
        y_pred=model.predict(x_range.reshape(-1,1))
        # Add regression line to scatter plot
        fig.add_trace(go.Scatter(x=x_range.flatten(),y=y_pred,mode='lines',
                                 line=dict(color='black',width=3),name='Trend'))
        # Show scatter plot in the column
        col.plotly_chart(fig,use_container_width=True)
