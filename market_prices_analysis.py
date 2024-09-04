import pandas as pd

from market_price_repository import MarketPriceRepository


def update_report():
    # extract data
    df = _extract_data()

    # Preprocessing
    df_day_ahead = df.loc[df["market"] == "Day-Ahead"]
    df_intraday = df.loc[df["market"] == "Intraday"]

    df_day_ahead = _reshape_data(df_day_ahead)
    df_intraday = _reshape_data(df_intraday)
    df = df_day_ahead.join(
        df_intraday, lsuffix="_dayAhead", rsuffix="_intraday", on="timestamp"
    )
    df = df[["price_dayAhead", "price_intraday"]]
    # compute percent changes
    df_pct_change = df.pct_change(fill_method=None).dropna()

    df.to_excel("/data/sheets/market_price.xlsx")
    df_pct_change.to_excel("/data/sheets/market_price_pct_changes.xlsx")
    print(df.head(20))


def _extract_data():
    market_price_repository = MarketPriceRepository()
    market_prices_data = market_price_repository.get_market_prices()
    df_market_prices = pd.DataFrame(market_prices_data)
    return df_market_prices


def _reshape_data(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="ISO8601")
    df = df.set_index("timestamp")
    df = df.drop("_id", axis=1)
    return df
