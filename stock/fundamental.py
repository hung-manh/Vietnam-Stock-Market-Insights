from .config import *

# Link để lấy các API stock: https://wifeed.vn/dashboard 
# Nếu không có thì các ông có thể tự tìm thêm nhé

def live_stock_list ():
    """
    Lấy thông tin cơ bản của các mã chứng khoán trên thị trường
    """
    url = "https://wifeed.vn/api/thong-tin-co-phieu/danh-sach-ma-chung-khoan?loaidn=1&san=HOSE"
    response = requests.request("GET", url).json()
    df = pd.DataFrame(response['data'])
    # rename columns fullname_vi to companyName, code to ticker, loaidn to companyType, san to exchange
    df = df.rename(columns={'fullname_vi': 'organName', 'code': 'ticker', 'loaidn': 'organTypeCode', 'san': 'comGroupCode'})
    return df




