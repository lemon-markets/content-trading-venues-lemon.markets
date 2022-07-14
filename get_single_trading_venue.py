import os
from dotenv import load_dotenv
from lemon import api


class SingleTradingVenue():

    def __init__(self):
        load_dotenv()
        self.client = api.create(
            market_data_api_token=os.getenv("DATA_API_KEY"),
            trading_api_token=os.getenv("TRADING_API_KEY"),
            env="paper"
    )

    def get_single_trading_venue(self):
        load_dotenv()
        mic = os.getenv("MIC")
        response = self.client.market_data.venues.get(mic=mic)
        print(response)


if __name__ == "__main__":
    SingleTradingVenue().get_single_trading_venue()

