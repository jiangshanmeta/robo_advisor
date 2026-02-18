import pandas as pd
import statsmodels.api as sm


def get_beta(stock_code: str):
    stock_prices = pd.read_csv(
        "data/stock_price.csv",
        index_col=0,
        parse_dates=True
    )
    mkt_prices = pd.read_csv(
        "data/market_price.csv",
        index_col=0,
        parse_dates=True
    )
    rf = pd.read_csv(
        "data/risk_free_rate.csv",
        index_col=0,
        parse_dates=True
    )
    stock_prices_monthly = stock_prices.resample('MS').first()  # get the first valid data of the month
    mkt_prices_monthly = mkt_prices.resample('MS').first()
    stock_returns_monthly = stock_prices_monthly[stock_code].pct_change()
    mkt_returns_monthly = mkt_prices_monthly.pct_change()

    y = (stock_returns_monthly - rf['TB3MS'] / 100 / 12).dropna()
    x = (mkt_returns_monthly['SPY'] - rf['TB3MS'] / 100 / 12).dropna()
    model = sm.OLS(y, x)
    results = model.fit()

    return results.params['x1']
