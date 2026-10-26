import pandas as pd
from typing import List
from schema import Coin


def load_prices(coins: List[Coin]) -> pd.DataFrame:
    """Read each coin's CSV back in and combine them into one DataFrame."""
    frames = []
    for coin in coins:
        df = pd.read_csv(f"{coin}.csv")
        df.insert(0, "coin", coin)
        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    # One row per coin, one column per currency
    return combined.pivot(index="coin", columns="currency", values="price")


def summarise_gbp(df: pd.DataFrame) -> dict:
    gbp = df["gbp"]
    return {
        "highest_coin": gbp.idxmax(),
        "highest_price": float(gbp.max()),
        "lowest_coin": gbp.idxmin(),
        "lowest_price": float(gbp.min()),
        "average_price": round(float(gbp.mean()), 2),
    }
