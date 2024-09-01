import requests


def fetch_data():
    url = "http://api-server:80/market_price"
    print(url)
    response = requests.get(url)
    print(response.json())


fetch_data()
