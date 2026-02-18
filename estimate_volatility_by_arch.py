import pandas as pd
from arch import arch_model

horizon = 63  # 63 days, 3 months
start_date = "2000-01-03"
end_date = "2022-05-24"


def estimate_volatility_by_arch(stock_code: str):
    price_pd = pd.read_csv(
        "data/stock_price.csv",
        index_col=0,
        parse_dates=True
    ).loc[start_date:end_date]

    returns = price_pd[stock_code].pct_change().dropna() * 100

    am = arch_model(returns)
    res = am.fit()
    forecasts = res.forecast(horizon=horizon)
    print(forecasts.residual_variance.iloc[-1, :])

    volatility_forecast = ((forecasts.residual_variance.iloc[-1, :].sum() * 252 / horizon) ** 0.5) / 100

    print(volatility_forecast)


if __name__ == "__main__":
    estimate_volatility_by_arch("AAPL")
