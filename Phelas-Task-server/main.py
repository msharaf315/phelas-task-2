from random import randrange, choice
from typing import Union
from datetime import datetime, timedelta
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/market_price")
def get_market_price(limit: int = 1):
    res = []
    for i in range(limit):
        timestamp = datetime.now() + timedelta(seconds=i)
        intraday_price_point = {
            "timestamp": timestamp,
            "price": randrange(100, 1000),
            "currency": "USD",
            "market": "Intraday",
        }
        day_ahead_price_point = {
            "timestamp": timestamp,
            "price": randrange(10, 500),
            "currency": "USD",
            "market": "Day-Ahead",
        }
        res.append(intraday_price_point)
        res.append(day_ahead_price_point)
        print(intraday_price_point, day_ahead_price_point)

    return res
