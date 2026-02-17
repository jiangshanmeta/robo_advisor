import numpy as np


def random_weights(n_assets: int):
    weights = np.random.randn(n_assets)
    return weights / sum(weights)

