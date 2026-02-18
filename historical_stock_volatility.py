import pandas as pd


def historical_volatility():
    stock_prices = pd.read_csv(
        "data/stock_price.csv",
        index_col=0,
        parse_dates=True
    )
    stock_returns = stock_prices.pct_change().dropna()
    stock_std_yearly = stock_returns.std() * (252 ** 0.5)
    stock_covariance_yearly = stock_returns.cov() * 252
    stock_correlation = stock_returns.corr()

    print(stock_std_yearly)
    print(stock_covariance_yearly)
    print(stock_correlation)

if __name__ == "__main__":
    historical_volatility()