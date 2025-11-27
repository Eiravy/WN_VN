import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

def data_analysis(df, theme_name, palette):
    st.header("1. Data Table")
    st.dataframe(df[['Country','Year','GDP_per_Capita','Life_Expectancy','Population','School_Enrollment']],use_container_width=True,height=500)
    st.header("2. Trends Over Time")
    metric = st.selectbox("Select Metric:", ['GDP_per_Capita','Life_Expectancy','Population','School_Enrollment'])
    fig_trend=px.line(df,x='Year',y=metric,color='Country',markers=True,
                      title=f"{metric} Trend Over Time",
                      template='plotly_dark' if theme_name=="Dark" else 'plotly_white')
    st.plotly_chart(fig_trend,use_container_width=True,height=500)
    st.header("3. Correlations")
    indicators = ['Life_Expectancy','Population','School_Enrollment']
    titles = ['Life Expectancy vs GDP','Population vs GDP','School Enrollment vs GDP']
    cols=st.columns(3)
    for col,y_var,t in zip(cols,indicators,titles):
        fig=px.scatter(df,x='GDP_per_Capita',y=y_var,color='Country',title=t,
                       template='plotly_dark' if theme_name=="Dark" else 'plotly_white',
                       color_discrete_sequence=palette)
        clean=df[['GDP_per_Capita',y_var]].dropna()
        X=clean[['GDP_per_Capita']]; y=clean[y_var]
        model=LinearRegression().fit(X,y)
        x_range=np.linspace(X.min(),X.max(),100)
        y_pred=model.predict(x_range.reshape(-1,1))
        fig.add_trace(go.Scatter(x=x_range.flatten(),y=y_pred,mode='lines',
                                 line=dict(color='black',width=3),name='Trend'))
        col.plotly_chart(fig,use_container_width=True)
