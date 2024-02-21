from .config import *
from . import config

'''
https://fc-data.ssi.com.vn/Help
'''
def get_securities_list(config=config, market='HOSE', page=1, page_size=100):
    client = fc_md_client.MarketDataClient(config)
    req = model.securities(market, page, page_size)
    # return client.securities(config, req)
    json = client.securities(config, req)
    return pd.DataFrame(json['data'])


def get_securities_details(config=config, market='HOSE', symbol='SSI', page=1, page_size=100):
    client = fc_md_client.MarketDataClient(config)
    req = model.securities_details(market, symbol, page, page_size)
    # return client.securities_details(config, req)
    json = client.securities_details(config, req)
    return pd.DataFrame(json['data'])



def get_index_list(config=config, market='', page=1, page_size=100):
    client = fc_md_client.MarketDataClient(config)
    req = model.index_list(market, page, page_size)
    # return client.index_list(config, req)
    json = client.index_list(config, req)
    return pd.DataFrame(json['data'])


def get_index_components(config=config, index='VN100', page=1, page_size=100):

    client = fc_md_client.MarketDataClient(config)
    req = model.index_components(index, page, page_size)
    # return client.index_components(config, req)
    json = client.index_components(config, req)
    return pd.DataFrame(json['data'])


def get_daily_OHLC(config=config, symbol='SSI', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100, ascending=True):
    client = fc_md_client.MarketDataClient(config)
    req = model.daily_ohlc(symbol, from_date, to_date,
                           page, page_size, ascending)
    # return client.daily_ohlc(config, req)
    json = client.daily_ohlc(config, req)
    return pd.DataFrame(json['data'])


def get_intraday_OHLC(config=config, symbol='SSI', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100, ascending=True, resolution=1):
	client = fc_md_client.MarketDataClient(config)
	req = model.intraday_ohlc(symbol, from_date, to_date, page, page_size, ascending, resolution)
	# return client.intraday_ohlc(config, req)
	json = client.intraday_ohlc(config, req)
	return pd.DataFrame(json['data'])
    
def get_daily_index(config=config, index='VN100', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100,   orderBy: str = '', order: str = ''):
    client = fc_md_client.MarketDataClient(config)
    req = model.daily_index(index, from_date, to_date,
                            page, page_size, orderBy, order)
    # return client.daily_index(config, req)
    json = client.daily_index(config, req)
    return pd.DataFrame(json['data'])


def get_daily_stock_price(config=config, symbol='SSI', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100, market='HOSE'):
    client = fc_md_client.MarketDataClient(config)
    req = model.daily_stock_price(
        symbol, from_date, to_date, page, page_size, market)
    # return client.daily_stock_price(config, req)
    json = client.daily_stock_price(config, req)
    return pd.DataFrame(json['data'])


def get_financial_ratio(symbol, report_range, is_all=False):
    """
    This function retrieves the essential financial ratios of a stock symbol on a quarterly or yearly basis. Some of the expected ratios include: P/E, P/B, ROE, ROA, BVPS, etc
    Args:
        symbol (:obj:`str`, required): 3 digits name of the desired stock.
        report_range (:obj:`str`, required): 'yearly' or 'quarterly'.
        is_all (:obj:`boo`, required): Set to True to retrieve all available years of data,  False to retrieve the last 5 years data (or the last 10 quarters). Default is True.
    """
    if report_range == 'yearly':
        x = 1
    elif report_range == 'quarterly':
        x = 0

    if is_all == True:
        y = 'true'
    else:
        y = 'false'

    data = requests.get(
        f'https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{symbol}/financialratio?yearly={x}&isAll={y}').json()
    df = json_normalize(data)
    # drop nan columns
    df = df.dropna(axis=1, how='all')
    # if report_range == 'yearly' then set index column to be df['year'] and drop quarter column, else set index to df['year'] + df['quarter']
    if report_range == 'yearly':
        df = df.set_index('year').drop(columns={'quarter'})
    elif report_range == 'quarterly':
        # add prefix 'Q' to quarter column
        df['quarter'] = 'Q' + df['quarter'].astype(str)
        # concatenate quarter and year columns
        df['range'] = df['quarter'].str.cat(df['year'].astype(str), sep='-')
        # move range column to the first column
        df = df[['range'] + [col for col in df.columns if col != 'range']]
        # set range column as index
        df = df.set_index('range')
    df = df.T
    return df


def get_financial_ratio_json(symbol, report_range, is_all=False):
    """
    This function retrieves the essential financial ratios of a stock symbol on a quarterly or yearly basis. Some of the expected ratios include: P/E, P/B, ROE, ROA, BVPS, etc
    Args:
        symbol (:obj:`str`, required): 3 digits name of the desired stock.
        report_range (:obj:`str`, required): 'yearly' or 'quarterly'.
        is_all (:obj:`boo`, required): Set to True to retrieve all available years of data,  False to retrieve the last 5 years data (or the last 10 quarters). Default is True.
    """
    if report_range == 'yearly':
        x = 1
    elif report_range == 'quarterly':
        x = 0

    if is_all == True:
        y = 'true'
    else:
        y = 'false'

    return requests.get(f'https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{symbol}/financialratio?yearly={x}&isAll={y}').json()
