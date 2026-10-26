from typing import List, Literal
from pydantic import BaseModel


Coin = Literal["bitcoin", "ethereum", "solana"]

class CoinPrice(BaseModel):
    currency: str
    price: float

class ApiResponse(BaseModel):
    coin: Coin
    prices: List[CoinPrice]
