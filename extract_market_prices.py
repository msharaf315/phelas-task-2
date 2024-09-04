import requests
import time
from market_price_repository import MarketPriceRepository
from market_prices_analysis import update_report


def fetch_data():
    # TODO env
    url = "http://api-server:80/market_price"
    # TODO fetch latest market price date and get prices afterwards
    res_body = requests.get(url).json()
    market_price_repository = MarketPriceRepository()
    market_price_repository.save_market_prices(res_body)
    update_report()
while True:
    time.sleep(20)
    try:
        fetch_data()
    except Exception as e:
        print(e)

fetch_data()
