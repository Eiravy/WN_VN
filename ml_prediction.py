import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.cluster import KMeans

def machinelearning_clustering(df, selected_countries, end_year):
    st.header("6. KMeans Clustering")
    avg_gdp=df.groupby('Country')['GDP_per_Capita'].mean().reset_index()
    K_value=st.slider("Select number of clusters:",2,min(10,len(avg_gdp)),3)
    kmeans=KMeans(n_clusters=K_value,random_state=42)
    avg_gdp['Cluster']=kmeans.fit_predict(avg_gdp[['GDP_per_Capita']])
    cluster_order=avg_gdp.groupby('Cluster')['GDP_per_Capita'].mean().sort_values().index
    cluster_labels={cluster:f"Cluster {i+1}" for i,cluster in enumerate(cluster_order)}
    avg_gdp['Cluster_Label']=avg_gdp['Cluster'].map(cluster_labels)
    fig_cluster=px.bar(avg_gdp.sort_values('GDP_per_Capita'),x='Country',y='GDP_per_Capita',
                       color='Cluster_Label',title="Countries Clustered by Average GDP per Capita",
                       template='plotly_white',color_discrete_sequence=px.colors.qualitative.Plotly)
    st.plotly_chart(fig_cluster,use_container_width=True)

    st.header("7. Predict Life Expectancy from GDP per Capita")
    methods={"Linear Regression":LinearRegression(),
             "Decision Tree":DecisionTreeRegressor(),
             "Random Forest":RandomForestRegressor()}
    test_start_year=end_year-9
    results=[]
    for country in selected_countries:
        c_data=df[df['Country']==country][['Year','GDP_per_Capita','Life_Expectancy']].dropna()
        if len(c_data)<2: continue
        X_train=c_data[c_data['Year']<test_start_year][['GDP_per_Capita']].values
        y_train=c_data[c_data['Year']<test_start_year]['Life_Expectancy'].values
        X_test=c_data[c_data['Year']>=test_start_year][['GDP_per_Capita']].values
        y_test=c_data[c_data['Year']>=test_start_year]['Life_Expectancy'].values
        if len(X_train)<1 or len(X_test)<1: continue
        row={"Country":country}
        for name, model in methods.items():
            m=model.__class__(**model.get_params())
            m.fit(X_train,y_train)
            y_pred=m.predict(X_test)
            row[name]=f"{mean_absolute_error(y_test,y_pred):.2f}"
        results.append(row)
        
    st.subheader("MAE for last 10 years")
    st.dataframe(pd.DataFrame(results).set_index("Country"),use_container_width=True)
    
    st.subheader("Predict Life Expectancy (Interactive)")
    input_gdp=st.number_input("Enter GDP per Capita (current US$):",min_value=0.0,value=10000.0,step=1000.0)
    selected_method=st.selectbox("Select ML Method:",list(methods.keys()))
    pred_country=st.selectbox("Select Country for Prediction:",selected_countries)
    c_data=df[df['Country']==pred_country][['GDP_per_Capita','Life_Expectancy']].dropna()
    if len(c_data)<2: st.warning("Not enough data for this country to train ML model.")
    else:
        X_train_full=c_data[['GDP_per_Capita']].values
        y_train_full=c_data['Life_Expectancy'].values
        model=methods[selected_method].__class__(**methods[selected_method].get_params())
        model.fit(X_train_full,y_train_full)
        predicted_life=model.predict([[input_gdp]])[0]
        st.success(f"Predicted Life Expectancy for {pred_country} with GDP ${input_gdp:,.0f}: **{predicted_life:.2f} years**")