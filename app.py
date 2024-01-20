import streamlit as st
from tabs import danh_sach_niem_yet, gioi_thieu, phan_tich_co_ban


# Set Streamlit app title 
st.title('Vietnam Stock Market Insights')


# Create tabs
tab1, tab2, tab3 = st.tabs(['Danh sách niêm yết', 'Phân tích cơ bản', 'Giới thiệu'])


with tab1:
    st.header('Danh sách niêm yết')
    danh_sach_niem_yet.render()

with tab2:
    st.header('Phân tích cơ bản')
    phan_tich_co_ban.render()

with tab3:
    st.header('Giới thiệu')
    gioi_thieu.render()



# import stock 

# # print(stock.get_securities_list(page_size=10))
# print(stock.get_daily_stock_price(from_date='18/01/2024', to_date='18/01/2024', page_size=10, market='HOSE'))