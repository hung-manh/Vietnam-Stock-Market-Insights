import streamlit as st 
import pandas as pd
import stock 


# DANH SÁCH NIÊM YẾT 
st.write('''
# Chứng khoán Việt Nam 
Hú ae vào đây xem thông tin cơ bản của các mã chứng khoán nhé''')

st.write('''## Danh sách các mã chứng khoán đã được niêm yết''')
st.write(stock.live_stock_list())   


# PHÂN TÍCH CƠ BẢN (Thông tin cơ bản của cổ phiếu, các chỉ số cơ bản và báo cáo tài chính)
# Code trong file fundamental.py


# PHÂN TÍCH KỸ THUẬT (Nơi vẽ các chart)


# LỰA CHỌN CỔ PHIẾU (CHỌN MUA, CHỌN BÁN)