import os
from lemon import api
from dotenv import load_dotenv


class TradingVenues():

    def __init__(self):
        load_dotenv()
        self.client = api.create(
            market_data_api_token=os.getenv("DATA_API_KEY"),
            trading_api_token=os.getenv("TRADING_API_KEY"),
            env="paper"
        )

    def get_all_trading_venues(self):
        response = self.client.market_data.venues.get()
        print(response)


if __name__ == "__main__":
    TradingVenues().get_all_trading_venues()
