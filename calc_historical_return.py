import pandas as pd


def calc_historical_return():
    df = pd.read_csv(
        "./stock_price.csv",
        index_col=0,
        parse_dates=True
    )

    stock_returns = df.pct_change().dropna()

    return stock_returns.mean() * 252
