import pandas as pd     # Import Pandas for data manipulation
import wbgapi as wb     # Import World Bank API

def data_loader(countries, start, end):
    # Define indicators to load from World Bank
    indicators = {'NY.GDP.PCAP.CD':'GDP_per_Capita',
                  'SP.DYN.LE00.IN':'Life_Expectancy',
                  'SP.POP.TOTL':'Population',
                  'SE.SEC.ENRR':'School_Enrollment'}
    
    dfs=[]      # Create an empty list to store the DataFrames
    # Loop through each indicator and its name
    for indicator_code, name in indicators.items():   
        # Get data for the indicator, for selected countries and years, include country labels, and reset the index
        df=wb.data.DataFrame(indicator_code,countries,range(start,end+1),labels=True).reset_index()  
        # Find columns that are years (either numbers or strings starting with 'YR')
        year_cols=[c for c in df.columns if isinstance(c,int) or (isinstance(c,str) and c.startswith('YR'))]   
        # Convert from wide format (one row per country, columns are years) to long format (one row per country-year)
        df_long=pd.melt(df,id_vars=['economy','Country'],value_vars=year_cols,
                        var_name='Year',value_name=name)    
        # Clean the Year column: get only the number and convert to integer    
        df_long['Year']=df_long['Year'].astype(str).str.extract(r'(\d+)').astype(int)       
        dfs.append(df_long)     # Add this long-format DataFrame to the list
        
    # Merge all indicators into one DataFrame by economy (country's code), country, and year
    df_all=dfs[0].merge(dfs[1],on=['economy','Country','Year']) \
                  .merge(dfs[2],on=['economy','Country','Year']) \
                  .merge(dfs[3],on=['economy','Country','Year'])
    
    # Return only the rows within the selected year range.
    return df_all[(df_all['Year']>=start) & (df_all['Year']<=end)]      
