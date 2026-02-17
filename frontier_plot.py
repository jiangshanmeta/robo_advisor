from typing import List

import matplotlib.pyplot as plt
import numpy as np

from portfolio import portfolio, covariance_matrix
from random_weights import random_weights


def plot_points(expected_returns: List[float], standard_deviations: List[float], stocks: List[str]):
    plt.figure(figsize=(8, 6))
    plt.scatter(standard_deviations, expected_returns, c="black")
    plt.xlim(0, 0.45)
    plt.ylim(0, 0.25)
    plt.ylabel("Mean")
    plt.xlabel("Standard Deviation")

    for i, stock in enumerate(stocks):
        plt.annotate(stock, (standard_deviations[i], expected_returns[i]), ha="center", va="bottom", weight="bold")


def plot_random_portfolio(
        weights: List[float],
        expected_returns: List[float],
        standard_deviations: List[float],
        correlation_matrix: List[List[float]],
        n_simulations: int
):
    n_assets = len(weights)

    mu_p_sims = []
    sigma_p_sims = []

    for i in range(n_simulations):
        w = random_weights(n_assets)
        mu_p, sigma_p = portfolio(expected_returns, standard_deviations, w, correlation_matrix)
        mu_p_sims.append(mu_p)
        sigma_p_sims.append(sigma_p)

    plt.scatter(sigma_p_sims, mu_p_sims, s=12)


def plot_minimum_variance_frontier(
        expected_returns: List[float],
        standard_deviations: List[float],
        correlation_matrix: List[List[float]]
):
    cov = covariance_matrix(standard_deviations, correlation_matrix)
    A, B, C = compute_ABC(expected_returns, cov)

    # bottom half
    y = np.linspace(0, B / A, 100)
    x = np.sqrt((A * y * y - 2 * B * y + C) / (A * C - B * B))
    plt.plot(x, y, color="green", lw=2.5, linestyle="--")

    # top half
    y = np.linspace(B / A, 0.45, 100)
    x = np.sqrt((A * y * y - 2 * B * y + C) / (A * C - B * B))
    plt.plot(x, y, color="red", lw=2.5, label="Efficient Frontier")


def compute_ABC(expected_returns: List[float], cov: List[List[float]]):
    cov_inv = np.linalg.inv(cov)
    ones = np.ones(len(expected_returns))
    A = ones @ cov_inv @ ones
    B = ones @ cov_inv @ expected_returns
    C = expected_returns @ cov_inv @ expected_returns
    return A, B, C

def plot_capital_allocation(
        rf:float,
        expected_returns: List[float],
        standard_deviations: List[float],
        correlation_matrix: List[List[float]]
):
    cov = covariance_matrix(standard_deviations, correlation_matrix)
    A, B, C = compute_ABC(expected_returns, cov)

    x = np.linspace(0,0.45,100)
    y = rf + x * (C-2*B*rf+A*rf**2) ** 0.5
    plt.plot(x,y,color="blue",lw=2.5)


