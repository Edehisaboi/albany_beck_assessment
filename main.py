from typing import List
from schema import Coin
from api import get_coin_price
from file import save_to_csv
from analysis import load_prices, summarise_gbp

COINS: List[Coin] = ["bitcoin", "ethereum", "solana"]


def main() -> int:
    # Core task: fetch each coin's price and save it to <coin>.csv
    for coin in COINS:
        try:
            result = get_coin_price(coin)
        except (RuntimeError, ValueError) as e:
            print(f"Error: {e}")
            return 1

        path = save_to_csv(result.coin, result.prices)
        print(f"Saved {path}")

    # Extension: read the CSVs back, combine them and summarise the GBP prices
    df = load_prices(COINS)
    summary = summarise_gbp(df)

    print(df)
    print(summary)
    return 0


if __name__ == "__main__":
    main()
