from .config import *

# Ở cái tab này thì tôi muốn hiển thị ra một cái bảng nến 
# Tôi viết ở stock file chart nhưng đang bị lỗi  


# cái tab này sẽ có các lựa chọn như sau
# - Chọn mã cổ phiếu 
# - Chọn thời gian
# - và cái biểu đồ nến thể hiện giá cổ phiếu theo thời gian với trục x là trục thời gian và trục y là giá cổ phiếu
# - và cái biểu đồ đường thể hiện giá đóng cửa của cổ phiếu 

def candlestick_part():
    tickers = stock.get_securities_list(page_size=1000)['Symbol'] # Lấy danh sách mã cổ phiếu
    with st.form(key='my_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            ticker = st.selectbox('Chọn mã cổ phiếu', tickers)
        with col2:
            from_date = st.date_input('Từ ngày', datetime.now(), format='DD/MM/YYYY').strftime('%d/%m/%Y')
        with col3:
            to_date = st.date_input('Đến ngày', datetime.now(), format='DD/MM/YYYY').strftime('%d/%m/%Y')
        col1, col2 = st.columns(2)
        with col1:
            ma_periods = st.checkbox('Moving Average')
        with col2:
            show_volume = st.checkbox('Volume') 
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write('You clicked the submit button')


    df = stock.get_daily_OHLC(symbol=ticker, from_date=from_date, to_date=to_date, page_size=1000)
    df['TradingDate'] = pd.to_datetime(df['TradingDate'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')
    fig = stock.candlestick_chart(df, title='Candlestick Chart with MA and Volume', x_label='Date', y_label='Price', ma_periods=ma_periods, show_volume=show_volume, figure_size=(10, 8), reference_period=None, colors=('#00F4B0', '#FF3747'), reference_colors=('blue', 'black'))
    st.write(fig)

def render():
    candlestick_part()