from .config import *

def render():
    st.write(stock.get_securities_list(market= '',page_size=1000))
    
