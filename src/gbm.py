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


if __name__ == "__main__":
    PERIOD_VOLATILITY = 0.0242  # daily volatility of fake stock
    STARTING_PRICE = 250.00  # starting stock price
    T = 252  # 252 trading days in a year

    NUM_SIMULATIONS = 1000

    price_list = gbm(STARTING_PRICE, PERIOD_VOLATILITY, T)  # list to store prices

    fig = plt.figure()
    fig.suptitle("Monte Carlo Simulation: MSFT")
    plt.plot(price_list)
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.show()

    df = pd.DataFrame()
    last_price_list = []
    for x in range(NUM_SIMULATIONS):
        price_list = gbm(STARTING_PRICE, PERIOD_VOLATILITY, T)
        df[x] = price_list
        last_price_list.append(price_list[-1])

    fig = plt.figure()
    fig.suptitle("Monte Carlo Simulation: MSFT")
    plt.plot(df)
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.show()

    print("Expected price: ", round(np.mean(last_price_list), 2))
    print("Quantile (5%): ", np.percentile(last_price_list, 5))
    print("Quantile (95%): ", np.percentile(last_price_list, 95))

    plt.hist(last_price_list, bins=100)
    plt.axvline(
        np.percentile(last_price_list, 5), color="r", linestyle="dashed", linewidth=2
    )
    plt.axvline(
        np.percentile(last_price_list, 95), color="r", linestyle="dashed", linewidth=2
    )
    plt.show()
