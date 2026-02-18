import yfinance as yf


def download_stock_data(tickers, csv_file_name):
    stock_data = yf.download(tickers, "2000-01-03", "2023-12-31", auto_adjust=False)
    if stock_data is not None:
        adj_data = stock_data["Adj Close"]
        adj_data.to_csv(csv_file_name)


if __name__ == '__main__':
    download_stock_data(["AAPL", "FE", "WMT"], "data/stock_price.csv")
    download_stock_data("SPY", "data/market_price.csv")
