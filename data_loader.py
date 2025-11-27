import pandas as pd
import wbgapi as wb

def data_loader(codes, start, end):
    indicators = {'NY.GDP.PCAP.CD':'GDP_per_Capita',
                  'SP.DYN.LE00.IN':'Life_Expectancy',
                  'SP.POP.TOTL':'Population',
                  'SE.SEC.ENRR':'School_Enrollment'}
    
    dfs=[]      # Create an empty list to store the Dataframes
    for code, name in indicators.items():   # Loop through each indicator and its name
        df=wb.data.DataFrame(code,codes,range(start,end+1),labels=True).reset_index()   # Get the World Bank data for the indicator and reset the index
        year_cols=[c for c in df.columns if isinstance(c,int) or (isinstance(c,str) and c.startswith('YR'))]    # Find all columns that represent years.
        df_long=pd.melt(df,id_vars=['economy','Country'],value_vars=year_cols,   # Change the data from wide format to long format.
                        var_name='Year',value_name=name)        
        df_long['Year']=df_long['Year'].astype(str).str.extract(r'(\d+)').astype(int)       # Extract the numeric year and convert it to an integer.
        dfs.append(df_long)     # Add this DataFrame to the list.
    # Merge all indicator DataFrames together by economy, country, and year.
    df_all=dfs[0].merge(dfs[1],on=['economy','Country','Year']) \
                  .merge(dfs[2],on=['economy','Country','Year']) \
                  .merge(dfs[3],on=['economy','Country','Year'])
    return df_all[(df_all['Year']>=start) & (df_all['Year']<=end)]      # Return only the rows within the selected year range.