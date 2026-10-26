import time
import requests
from schema import ApiResponse, Coin, CoinPrice

ENDPOINT = "https://api.coingecko.com/api/v3/simple/price"
MAX_RETRIES = 3


def get_coin_price(coin: Coin, currencies: str = "gbp,usd,eur") -> ApiResponse:
    if not coin:
        raise ValueError("Coin is required")

    params = {"ids": coin, "vs_currencies": currencies}

    try:
        # The free CoinGecko API rate-limits aggressively, so back off and retry on 429 (Too many requests)
        # unlikely for this case though
        response = requests.get(ENDPOINT, params=params, timeout=10)
        for attempt in range(MAX_RETRIES):
            if response.status_code != 429:
                break
            # Prefer the server's Retry-After hint, otherwise fall back to exponential backoff
            retry_after = response.headers.get("Retry-After", "")
            time.sleep(int(retry_after) if retry_after.isdigit() else 2 ** (attempt + 1))
            response = requests.get(ENDPOINT, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch price for {coin}: {e}") from e

    # CoinGecko returns: {"solana": {"gbp": 140.23, "usd": 185.67, "eur": 170.45}}
    coin_data = data.get(coin)
    if not coin_data:
        raise ValueError(f"No data returned for coin: {coin}")

    prices = [
        CoinPrice(currency=curr, price=price)
        for curr, price in coin_data.items()
    ]

    return ApiResponse(coin=coin, prices=prices)
