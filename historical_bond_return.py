import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

CORPORATE_BOND_CODE = "BAMLCC8A015PYTRIV"
SHORT_TERM_RF_CODE =  "DTB3"
TREASURY_BOND_CODE = "DGS10"

def plot_treasury_monthly_yield():
    treasury_df = pd.read_csv("data/treasury_bond_yield.csv", index_col=0, parse_dates=True)
    treasury_df.plot(xlabel="Date", ylabel="Yield on 10-Year Treasuries", legend=False)
    plt.show()


def historical_bond_return():
    bond_df = pd.read_csv("data/corporate_bond.csv",index_col=0,parse_dates=True)
    bond_monthly = bond_df.resample("ME").last()
    bond_return_monthly = bond_monthly.pct_change()

    treasury_df = pd.read_csv("data/treasury_bond_yield.csv", index_col=0, parse_dates=True)
    treasury_monthly = treasury_df.resample("ME").last()
    treasury_change_monthly = treasury_monthly.diff().dropna()/100.0

    rf_df = pd.read_csv("data/short_term_risk_free_rate.csv",index_col=0,parse_dates=True)
    rf_monthly = rf_df.resample("ME").last() / 100

    print("raw bond average return ", bond_return_monthly[CORPORATE_BOND_CODE].mean()*12)
    print("excess bond average return ", (bond_return_monthly[CORPORATE_BOND_CODE]-rf_monthly[SHORT_TERM_RF_CODE].shift()/12 ).mean()*12  )

    Y = (bond_return_monthly[CORPORATE_BOND_CODE] - rf_monthly[SHORT_TERM_RF_CODE].shift()/12  ).dropna()
    X = sm.add_constant(treasury_change_monthly)
    common_dates  = X.index.intersection(Y.index)
    X = X.loc[common_dates]
    model = sm.OLS(Y, X)
    results = model.fit()
    print("OLS results: ", results.summary())
    #  企业债券超出10年Treasury 的 yield
    print("The expected return after stripping out yield changes is ", results.params.iloc[0] * 12)

    plt.plot(X[TREASURY_BOND_CODE], results.fittedvalues, color='red')
    plt.scatter(X[TREASURY_BOND_CODE], Y)
    plt.xlabel('Change 10Yr Yield')
    plt.ylabel('Returns')
    plt.title('Regression Line')
    plt.show()

if __name__ == "__main__":
    historical_bond_return()
