from .config import *
from .phan_tich_ky_thuat import get_date_range

def thong_tin_co_ban():
    st.subheader('Thông tin cơ bản')
    tickers = stock.get_securities_list(page_size=1000)['Symbol']  # Lấy danh sách mã cổ phiếu   
    ticker = st.selectbox('Chọn mã cổ phiếu', tickers, key='select_ticker')

    col1, col2 = st.columns(2)

    with col1:
        securities_details = stock.get_securities_details(symbol=ticker)
        index_components = stock.get_index_components()
        from_date, to_date = get_date_range('1 ngày')
        daily_stock_price = stock.get_daily_stock_price(symbol=ticker, from_date=from_date, to_date=to_date, page_size=1000 )

        index_components=index_components.drop(columns=['IndexComponent'])
        securities_details=securities_details.drop(columns=['RepeatedInfo'])
        
        st.write(f"Thông tin về {ticker}:")
        st.write(securities_details)
        st.write(f"Các thành phần của chỉ số VN100:")
        st.write(index_components)
        st.write(f"Giá cổ phiếu hàng ngày của {ticker}:")
        st.write(daily_stock_price)
        
    with col2:
        pass


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