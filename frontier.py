import matplotlib.pyplot as plt

from frontier_plot import plot_points, plot_random_portfolio, plot_minimum_variance_frontier,plot_capital_allocation

stocks = ["FE", "WMT", "AAPL"]
mu = [0.04, 0.09, 0.12]
sigma = [0.15, 0.2, 0.35]
weights = [0.2, 0.3, 0.5]

correlation_matrix = [
    [1.0, 0.1, 0.17],
    [0.1, 1.0, 0.26],
    [0.17, 0.26, 1.0]
]

rf = 0.02

if __name__ == "__main__":
    plot_points(mu, sigma, stocks)
    plot_random_portfolio(
        weights,
        mu,
        sigma,
        correlation_matrix,
        1000
    )
    plot_minimum_variance_frontier(mu, sigma, correlation_matrix)
    plot_capital_allocation(rf,mu, sigma, correlation_matrix)
    plt.show()
