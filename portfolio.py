from typing import List

import numpy as np


def portfolio_expected_return(expected_returns: List[float], weights: List[float]):
    w = np.array(weights)
    return np.array(expected_returns) @ w.T


def covariance_matrix(standard_deviations: List[float], correlation_matrix: List[List[float]]):
    return np.diag(standard_deviations) @ correlation_matrix @ np.diag(standard_deviations)


def portfolio_standard_deviation(standard_deviations: List[float], weights: List[float],
                                 correlation_matrix: List[List[float]]):
    cov = covariance_matrix(standard_deviations, correlation_matrix)
    w = np.array(weights)
    return (w @ cov @ w.T) ** 0.5


def portfolio(expected_returns: List[float], standard_deviations: List[float], weights: List[float],
              correlation_matrix: List[List[float]]):
    return portfolio_expected_return(expected_returns, weights), portfolio_standard_deviation(standard_deviations,
                                                                                              weights,
                                                                                              correlation_matrix)
