import streamlit as st
import pandas as pd
from .config import *

def render():   
    df = pd.read_csv('tabs/stock.csv')
    df = df[['ticker','exchange','shortName','industry','industryEn','establishedYear','noEmployees','noShareholders','foreignPercent','website','stockRating','deltaInWeek','deltaInMonth','deltaInYear','outstandingShare','issueShare',]]
    df = df.dropna(subset=['ticker'])
    
    with st.form(key='stock_form'):
        industry_options = df['industry'].tolist() + ['Tất cả']
        selected_industries = st.multiselect('Chọn ngành', industry_options)
        stock_rating = st.selectbox('Xếp hạng', ['Mặc định', 'Tăng dần', 'Giảm dần'])
        
        button = st.form_submit_button('Submit')

    if button:
        if selected_industries:
            df = df[df['industry'].isin(selected_industries)]
        if stock_rating == 'Tăng dần':
            df = df.sort_values('stockRating', ascending=True)
        elif stock_rating == 'Giảm dần':
            df = df.sort_values('stockRating', ascending=False)
        
    df = df.reset_index(drop=True)
    st.write(df)
 
