from .config import *

def thong_tin_co_ban():
    st.subheader('Thông tin cơ bản')

def chi_so_co_ban():   
    st.subheader('Chỉ số cơ bản')

def bao_cao_tai_chinh():    
    st.subheader('Báo cáo tài chính')
    
def render():
    thong_tin_co_ban()
    st.markdown('---')
    chi_so_co_ban()
    st.markdown('---')
    bao_cao_tai_chinh()