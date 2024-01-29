from .config import *

def thong_tin_co_ban():
    st.subheader('Thông tin cơ bản')
    tickers = stock.get_securities_list(page_size=1000)['Symbol'] # Lấy danh sách mã cổ phiếu


def chi_so_co_ban():   
    st.subheader('Chỉ số cơ bản')
    tickers = stock.get_securities_list(page_size=1000)['Symbol'] # Lấy danh sách mã cổ phiếu   
    col1, col2 = st.columns(2)
    with col1:
        ticker = st.selectbox('Chọn mã cổ phiếu', tickers)
    with col2:
        report_range = st.selectbox('Chọn kỳ báo cáo', ['Quý', 'Năm'])
        if report_range == 'Quý':
            report_range = 'quarterly'
        else:
            report_range = 'yearly'
    st.write(stock.get_financial_ratio(ticker, report_range))

def bao_cao_tai_chinh():    
    st.subheader('Báo cáo tài chính')
    
def render():
    thong_tin_co_ban()
    st.markdown('---')
    chi_so_co_ban()
    st.markdown('---')
    bao_cao_tai_chinh()