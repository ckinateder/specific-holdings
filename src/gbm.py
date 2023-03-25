import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def gbm(
    starting_price: float,
    volatility: float = 0.02459,
    t: int = 252,
) -> list:
    """Generate geometric brownian motion (GBM) for a fictional commodity.
    Can be used to model for any equal time period.

    Args:
        starting_price (float): starting price of a commodity.
        volatility (float, optional): volatility for the created set. Defaults to 0.02459.
        t (int, optional): size of returned array. Defaults to 252.

    Returns:
        list: list of prices for the fictional commodity.
    """
    prices = [starting_price]
    for l in range(1, t):
        price = prices[l - 1] * (1 + np.random.normal(0, volatility))
        prices.append(price)
    return prices
