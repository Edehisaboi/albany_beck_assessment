import pandas as pd
from typing import List
from schema import Coin, CoinPrice

def save_to_csv(coin: Coin, prices: List[CoinPrice]) -> str:
    if not coin:
        raise ValueError("Coin is required")
    if not prices:
        raise ValueError("No prices to save")

    # Convert to DataFrame
    df = pd.DataFrame([
        {"currency": p.currency, "price": p.price}
        for p in prices
    ])
    df.to_csv(f"{coin}.csv", index=False)
    return f"{coin}.csv"
