from .config import *


@st.cache_resource()
def thong_tin_co_ban():
    st.subheader('Thông tin cơ bản')
    return stock.get_securities_list(
        page_size=1000)['Symbol']  # Lấy danh sách mã cổ phiếu


def chi_so_co_ban():
    st.subheader('Chỉ số cơ bản')
    tickers = stock.get_securities_list(
        page_size=1000)['Symbol']  # Lấy danh sách mã cổ phiếu
    col1, col2, col3 = st.columns(3)
    with col1:
        ticker = st.selectbox('Chọn mã cổ phiếu', tickers)
    with col2:
        report_range = st.selectbox('Chọn kỳ báo cáo', ['Quý', 'Năm'])
        if report_range == 'Quý':
            report_range = 'quarterly'
            n_report_range = '0'
        else:
            report_range = 'yearly'
            n_report_range = '1'
    st.write(stock.get_financial_ratio(ticker, report_range))
    with col3:
        index = st.selectbox('Your choice: ', ["priceToEarning",
                                               "priceToBook"
                                               "valueBeforeEbitda",
                                               "dividend",
                                               "roe",
                                               "roa",
                                               "daysReceivable",
                                               "daysInventory",
                                               "daysPayable",
                                               "ebitOnInterest",
                                               "earningPerShare",
                                               "bookValuePerShare",
                                               "interestMargin",
                                               "nonInterestOnToi",
                                               "badDebtPercentage",
                                               "provisionOnBadDebt",
                                               "costOfFinancing",
                                               "equityOnTotalAsset",
                                               "equityOnLoan",
                                               "costToIncome",
                                               "equityOnLiability",
                                               "currentPayment",
                                               "quickPayment",
                                               "epsChange",
                                               "ebitdaOnStock",
                                               "grossProfitMargin",
                                               "operatingProfitMargin",
                                               "postTaxMargin",
                                               "debtOnEquity",
                                               "debtOnAsset",
                                               "debtOnEbitda",
                                               "shortOnLongDebt",
                                               "assetOnEquity",
                                               "capitalBalance",
                                               "cashOnEquity",
                                               "cashOnCapitalize",
                                               "cashCirculation",
                                               "revenueOnWorkCapital",
                                               "capexOnFixedAsset",
                                               "revenueOnAsset",
                                               "postTaxOnPreTax",
                                               "ebitOnRevenue",
                                               "preTaxOnEbit",
                                               "preProvisionOnToi",
                                               "postTaxOnToi",
                                               "loanOnEarnAsset",
                                               "loanOnAsset",
                                               "loanOnDeposit",
                                               "depositOnEarnAsset",
                                               "badDebtOnAsset",
                                               "liquidityOnLiability",
                                               "payableOnEquity",
                                               "cancelDebt",
                                               "ebitdaOnStockChange",
                                               "bookValuePerShareChange",
                                               "creditGrowth"])

    data = requests.get(
        f'https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{ticker}/financialratio?yearly={n_report_range}&isAll=false').json()

    # Extracting data for the chart
    df = pd.DataFrame(data)
    years = [entry['year'] for entry in data]
    finace_ratios = [entry[index] for entry in data]
    df = df[::-1]
    # pb_ratios = [entry['priceToBook'] for entry in data]

    # Plotting the data
    fig, ax = plt.subplots()
    if n_report_range == '0':
        df['quarter_label'] = 'Q' + \
            df['quarter'].astype(str) + ' ' + df['year'].astype(str)
        ax.plot(df['quarter_label'], df[index], color='skyblue')

        # Adding labels and title
        ax.set_xlabel('Quarter')
        ax.set_ylabel('Ratio')
        ax.set_title('Finace ratio to analyze')
        ax.legend()

        # Streamlit app
        st.title('Price to Earning Over Quarter by Years')
        st.pyplot(fig)

    elif n_report_range == '1':
        ax.plot(years, finace_ratios, label=index)
        # Adding labels and title
        ax.set_xlabel('Years')
        ax.set_ylabel('Ratio')
        ax.set_title('Finace ratio to analyze')
        ax.legend()

    # Streamlit app
        st.subheader('Stock Ratios Over Years')
        st.pyplot(fig)


def bao_cao_tai_chinh():
    st.subheader('Báo cáo tài chính')


def render():
    option = st.selectbox('Chose a company', stock.get_securities_list(
        page_size=1000)['Symbol'])

    @st.cache_resource()
    def display_infor():
        infor = requests.get(
            f'https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{option}/overview').json()
        if isinstance(infor, dict):
            # Check if the API response is a dictionary
            # Convert the dictionary to a DataFrame
            infor = pd.DataFrame([infor])
        else:
            # If it's already a list or another suitable structure, create the DataFrame directly
            infor = pd.DataFrame(infor)

        infor = infor.T.reset_index()  # Transpose the DataFrame and reset the index
        return infor
    st.write(display_infor())
    st.markdown('---')
    chi_so_co_ban()

    st.markdown('---')
    bao_cao_tai_chinh()
