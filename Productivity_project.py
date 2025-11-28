
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(layout= 'wide', page_title= 'Productivity Project')

html_title = """<h1 style="color:white;text-align:center;"> Employees Productivity Project </h1>"""
st.markdown(html_title, unsafe_allow_html=True)
df = pd.read_csv('Cleaned_df.csv',index_col = 0)
st.dataframe(df)
#st.image('https://news.blr.com/app/uploads/sites/3/2019/10/improve-productivity.jpg')
page = st.sidebar.radio('pages',['univariate','bivariate','multivariate'])

if page == 'univariate':
    st.title('univariate')
    for col in df.columns:  
        st.plotly_chart(px.histogram(data_frame = df,x = col , title = col))

elif page == 'bivariate' :
    st.plotly_chart(px.scatter(data_frame = df , x = 'team',y = 'actual_productivity'))
    st.plotly_chart(px.box(data_frame = df , x = 'department',y = 'actual_productivity'))
    prod_per_month = (df.groupby('month')['actual_productivity'].mean().sort_values(ascending = False)).reset_index()
    st.plotly_chart(px.bar(data_frame = prod_per_month , x = 'month',y = 'actual_productivity',title = 'what is the average productivity for each month ?'))
    
elif page == 'multivariate' :
    prod_per_month_per_dept = (df.groupby(['month','department'])['actual_productivity'].mean().sort_values(ascending = False)).reset_index()
    st.plotly_chart(px.bar(data_frame = prod_per_month_per_dept ,x = 'month', y = 'actual_productivity',color = 'department',title = 'what is the average productivity per month per department',barmode = 'group'))

    
    
