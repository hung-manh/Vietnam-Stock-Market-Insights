import streamlit as st
from tabs import danh_sach_niem_yet, gioi_thieu, phan_tich_co_ban, phan_tich_ky_thuat, chon_lua_co_phieu

st.set_page_config(layout="wide", 
                   initial_sidebar_state="collapsed",
                   page_title='Vietnam Stock Market Insights',
                   page_icon=':chart_with_upwards_trend:'
                   )


# Set Streamlit app title 
st.title('Vietnam Stock Market Insights')

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Danh sách niêm yết', 'Phân tích cơ bản', 'Phân tích kỹ thuật', 'Chọn lựa cổ phiếu','Giới thiệu'])

with tab1:
    st.header('Danh sách niêm yết')
    danh_sach_niem_yet.render()

with tab2:
    st.header('Phân tích cơ bản')
    phan_tich_co_ban.render()

with tab3:
    st.header('Phân tích kỹ thuật')
    phan_tich_ky_thuat.render()

with tab4:
    st.header('Chọn lựa cổ phiếu')
    chon_lua_co_phieu.render() # This tab is under development

    
with tab5:
    st.header('Giới thiệu')
    gioi_thieu.render()