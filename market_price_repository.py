from pymongo import MongoClient


class MarketPriceRepository:
    def __init__(self):
        # TODO env
        db_client = MongoClient("mongodb://root:example@mongo:27017/", port=27017)
        db = db_client.phelas_task
        self.market_prices = db.market_prices

    def save_market_prices(self, prices_list: list):
        self.market_prices.insert_many(prices_list)

    def get_market_prices(self):
        return self.market_prices.find().sort("timestamp")

    def get_latest_market_price_date():
        # TODO
        pass
