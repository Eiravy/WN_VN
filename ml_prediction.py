import streamlit as st      # Import Streamlit for web app
import pandas as pd     # Import Pandas for data manipulation
import plotly.express as px     # Import Plotly Express for plotting
from sklearn.linear_model import LinearRegression       # ML model
from sklearn.tree import DecisionTreeRegressor      # ML model
from sklearn.ensemble import RandomForestRegressor      # ML model
from sklearn.metrics import mean_absolute_error     # To measure prediction error
from sklearn.cluster import KMeans      # Clustering

def machinelearning_clustering(df, selected_countries, end_year):
    st.header("6. KMeans Clustering")
    # Compute average GDP per Capita per country
    avg_gdp=df.groupby('Country')['GDP_per_Capita'].mean().reset_index()
    # Slider to select number of clusters
    K_value=st.slider("Select number of clusters:",2,min(10,len(avg_gdp)),3)
    # KMeans clustering
    kmeans=KMeans(n_clusters=K_value,random_state=42)
    avg_gdp['Cluster']=kmeans.fit_predict(avg_gdp[['GDP_per_Capita']])
    # Order clusters by GDP
    cluster_order=avg_gdp.groupby('Cluster')['GDP_per_Capita'].mean().sort_values().index
    cluster_labels={cluster:f"Cluster {i+1}" for i,cluster in enumerate(cluster_order)}
    avg_gdp['Cluster_Label']=avg_gdp['Cluster'].map(cluster_labels)
    # Bar chart of countries colored by cluster
    fig_cluster=px.bar(avg_gdp.sort_values('GDP_per_Capita'),x='Country',y='GDP_per_Capita',
                       color='Cluster_Label',title="Countries Clustered by Average GDP per Capita",
                       template='plotly_white',color_discrete_sequence=px.colors.qualitative.Plotly)
    st.plotly_chart(fig_cluster,use_container_width=True)


    st.header("7. Predict Life Expectancy from GDP per Capita")
    # Define ML methods
    methods={"Linear Regression":LinearRegression(),
             "Decision Tree":DecisionTreeRegressor(),
             "Random Forest":RandomForestRegressor()}
    test_start_year=end_year-9      # Last 10 years for testing
    results=[]
    
    # Loop over selected countries to calculate MAE
    for country in selected_countries:
        # Get data for this country
        c_data=df[df['Country']==country][['Year','GDP_per_Capita','Life_Expectancy']].dropna()
        if len(c_data)<2: continue      # Skip if not enough data
        # Split train/test based on year
        X_train=c_data[c_data['Year']<test_start_year][['GDP_per_Capita']].values
        y_train=c_data[c_data['Year']<test_start_year]['Life_Expectancy'].values
        X_test=c_data[c_data['Year']>=test_start_year][['GDP_per_Capita']].values
        y_test=c_data[c_data['Year']>=test_start_year]['Life_Expectancy'].values
        if len(X_train)<1 or len(X_test)<1: continue       # Skip if empty
        row={"Country":country}
        # Fit each ML model and calculate MAE
        for name, model in methods.items():
            m=model.__class__(**model.get_params())     # Create new model instance
            m.fit(X_train,y_train)      # Train model
            y_pred=m.predict(X_test)    # Predict
            row[name]=f"{mean_absolute_error(y_test,y_pred):.2f}"      # Store MAE
        results.append(row)
        
    # Show MAE table
    st.subheader("MAE for last 10 years")
    st.dataframe(pd.DataFrame(results).set_index("Country"),use_container_width=True)
    
    # Interactive Life Expectancy prediction
    st.subheader("Predict Life Expectancy (Interactive)")
    input_gdp=st.number_input("Enter GDP per Capita (current US$):",min_value=0.0,value=10000.0,step=1000.0)
    selected_method=st.selectbox("Select ML Method:",list(methods.keys()))
    pred_country=st.selectbox("Select Country for Prediction:",selected_countries)
    # Get data for selected country
    c_data=df[df['Country']==pred_country][['GDP_per_Capita','Life_Expectancy']].dropna()
    if len(c_data)<2: st.warning("Not enough data for this country to train ML model.")
    else:
        # Train model on full country data
        X_train_full=c_data[['GDP_per_Capita']].values
        y_train_full=c_data['Life_Expectancy'].values
        model=methods[selected_method].__class__(**methods[selected_method].get_params())
        model.fit(X_train_full,y_train_full)
        # Predict life expectancy for input GDP
        predicted_life=model.predict([[input_gdp]])[0]
        st.success(f"Predicted Life Expectancy for {pred_country} with GDP ${input_gdp:,.0f}: **{predicted_life:.2f} years**")
