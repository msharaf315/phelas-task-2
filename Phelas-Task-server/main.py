from random import randrange, choice
from typing import Union
from datetime import datetime, timedelta
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/market_price")
def get_market_price(date: datetime = datetime.now(), limit: int = 5):
    res = []
    for i in range(limit):
        intraday_price_point = {
            "timestamp": date + timedelta(minutes=i),
            "price": randrange(10, 1000),
            "currency": "USD",
            "market": "Intraday",
        }
        day_ahead_price_point = {
            "timestamp": date + timedelta(minutes=i),
            "price": randrange(10, 1000),
            "currency": "USD",
            "market": "Day-Ahead",
        }
        res.append(intraday_price_point)
        res.append(day_ahead_price_point)

    return res
