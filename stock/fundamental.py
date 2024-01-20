from .config import *
from . import config

client = fc_md_client.MarketDataClient(config)

def get_securities_list(market='HOSE', page=1, page_size=100):
	req = model.securities(market, page, page_size)
	# return client.securities(config, req)
	json = client.securities(config, req) 
	return pd.DataFrame(json['data'])

def get_securities_details(market='HOSE', symbol='SSI', page=1, page_size=100):
	req = model.securities_details(market, symbol, page, page_size)
	return client.securities_details(config, req)

def get_index_list(market='', page=1, page_size=100):
	req = model.index_list(market, page, page_size)
	return client.index_list(config, req)

def get_index_components(index='VN100', page=1, page_size=100):
	req = model.index_components(index, page, page_size)
	return client.index_components(config, req)

def get_daily_OHLC(symbol='SSI', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100, ascending=True):
	req = model.daily_ohlc(symbol, from_date, to_date, page, page_size, ascending)
	return client.daily_ohlc(config, req)

def get_intraday_OHLC(symbol='SSI', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100, ascending=True, resolution=1):
	req = model.intraday_ohlc(symbol, from_date, to_date, page, page_size, ascending, resolution)
	return client.intraday_ohlc(config, req)

def get_daily_index(index='VN100', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100,   orderBy: str = '', order: str = ''):
	req = model.daily_index(index, from_date, to_date, page, page_size, orderBy, order)
	return client.daily_index(config, req)

def get_daily_index(index='VN100', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100,   orderBy: str = '', order: str = ''):
	req = model.daily_index(index, from_date, to_date, page, page_size, orderBy, order)
	return client.daily_index(config, req)

def get_daily_stock_price(symbol='SSI', from_date='15/10/2020', to_date='15/10/2020', page=1, page_size=100, market='HOSE'):
	req = model.daily_stock_price(symbol, from_date, to_date, page, page_size, market)
	return client.daily_stock_price(config, req)