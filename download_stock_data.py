import yfinance as yf

def download_stock_data():
    stock_data = yf.download(["AAPL", "FE", "WMT"], "2000-01-03", "2023-12-31",auto_adjust=False)
    if stock_data is not None:
        adj_data = stock_data["Adj Close"]
        adj_data.to_csv("stock_price.csv")

if __name__ == '__main__':
    download_stock_data()