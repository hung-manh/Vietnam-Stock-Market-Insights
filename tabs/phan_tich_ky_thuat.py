from .config import *
from datetime import datetime, timedelta

# cái tab này sẽ có các lựa chọn như sau
# - Chọn mã cổ phiếu 
# - Chọn thời gian
# - và cái biểu đồ nến thể hiện giá cổ phiếu theo thời gian với trục x là trục thời gian và trục y là giá cổ phiếu
# - và cái biểu đồ đường thể hiện giá đóng cửa của cổ phiếu 

def get_date_range(time_frame):
    if time_frame == '1 ngày':
        from_date = to_date = datetime.now().strftime('%d/%m/%Y')
    elif time_frame == '1 tuần':
        from_date = (datetime.now() - timedelta(days=7)).strftime('%d/%m/%Y')
        to_date = datetime.now().strftime('%d/%m/%Y')
    elif time_frame == '1 tháng':
        from_date = (datetime.now() - timedelta(days=30)).strftime('%d/%m/%Y')
        to_date = datetime.now().strftime('%d/%m/%Y')
    elif time_frame == '3 tháng':
        from_date = (datetime.now() - timedelta(days=90)).strftime('%d/%m/%Y')
        to_date = datetime.now().strftime('%d/%m/%Y')
    elif time_frame == '6 tháng':
        from_date = (datetime.now() - timedelta(days=180)).strftime('%d/%m/%Y')
        to_date = datetime.now().strftime('%d/%m/%Y')
    elif time_frame == '1 năm':
        from_date = (datetime.now() - timedelta(days=365)).strftime('%d/%m/%Y')
        to_date = datetime.now().strftime('%d/%m/%Y')
    else:
        col1 , col2 =st.columns(2)
        with col1:
            from_date = st.date_input('Từ ngày', datetime.now() - timedelta(days=60), format='DD/MM/YYYY').strftime('%d/%m/%Y')
        with col2:
            to_date = st.date_input('Đến ngày', datetime.now(), format='DD/MM/YYYY').strftime('%d/%m/%Y')
    return from_date, to_date

def fetch_data(ticker, from_date, to_date):
    try:
        if from_date != to_date:
            return stock.get_daily_OHLC(symbol=ticker, from_date=from_date, to_date=to_date, page_size=1000)
        else:
            return stock.get_intraday_OHLC(symbol=ticker, from_date=from_date, to_date=to_date, page_size=500)
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def render():
    tickers = stock.get_securities_list(page_size=1000)['Symbol']  # Lấy danh sách mã cổ phiếu

    # Use container instead of sidebar

    col1, col2 = st.columns([2.5,8])

    with col1:
        with st.form(key='technical_analysis_form'):
            ticker = st.selectbox('Chọn mã cổ phiếu', tickers)
            time_frame = st.selectbox('Chọn thời gian', ['1 tuần', '1 tháng', '3 tháng', '6 tháng', '1 năm', '3 năm', 'Tự chọn'], index=1)

            from_date, to_date = get_date_range(time_frame)

            is_ma_periods = st.selectbox('Đường trung bình động (MA)', ['No', 'Yes'])
            if is_ma_periods == 'Yes':
                ma_periods = st.slider('MA Periods', min_value=1, max_value=100, value=5)
                ma_periods = [ma_periods]
            else:
                ma_periods = None

            # is_reference_period = st.selectbox('Reference Period', ['No', 'Yes'])
            # if is_reference_period == 'Yes':
            #     reference_period = st.slider('reference_period', min_value=1, max_value=100, value=5)
            # else:
            #     reference_period = None
            submit_button = st.form_submit_button(label='Submit')

    with col2:
        # Display the candlestick chart if the form is submitted
        if submit_button:
            data = fetch_data(ticker, from_date, to_date)
            if data is not None:
                st.subheader('Biểu đồ nến')
                data['TradingDate'] = pd.to_datetime(data['TradingDate'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')
                fig = stock.candlestick_chart_ver1(data, title='Candlestick Chart of ' + ticker, x_label='Date', y_label='Price', ma_periods=ma_periods,  figure_size=(8.5, 6), reference_period=None, colors=('#00F4B0', '#FF3747'), reference_colors=('blue', 'black'))
                st.plotly_chart(fig)

                # Dữ liệu bảng
                st.markdown('---')
                st.subheader('Dữ liệu bảng') 
                st.write(data)        