import pandas as pd
import wbgapi as wb

def data_loader(codes, start, end):
    indicators = {'NY.GDP.PCAP.CD':'GDP_per_Capita',
                  'SP.DYN.LE00.IN':'Life_Expectancy',
                  'SP.POP.TOTL':'Population',
                  'SE.SEC.ENRR':'School_Enrollment'}
    dfs=[]
    for code, name in indicators.items():
        df=wb.data.DataFrame(code,codes,range(start,end+1),labels=True).reset_index()
        year_cols=[c for c in df.columns if isinstance(c,int) or (isinstance(c,str) and c.startswith('YR'))]
        df_long=pd.melt(df,id_vars=['economy','Country'],value_vars=year_cols,
                        var_name='Year',value_name=name)
        df_long['Year']=df_long['Year'].astype(str).str.extract(r'(\d+)').astype(int)
        dfs.append(df_long)
    df_all=dfs[0].merge(dfs[1],on=['economy','Country','Year']) \
                  .merge(dfs[2],on=['economy','Country','Year']) \
                  .merge(dfs[3],on=['economy','Country','Year'])
    return df_all[(df_all['Year']>=start) & (df_all['Year']<=end)]