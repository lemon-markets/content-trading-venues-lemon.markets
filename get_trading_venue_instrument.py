import os
from dotenv import load_dotenv
from lemon import api


class TradingVenueInstrument():

    def __init__(self):
        load_dotenv()
        self.client = api.create(
            market_data_api_token=os.getenv("DATA_API_KEY"),
            trading_api_token=os.getenv("TRADING_API_KEY"),
            env="paper"
    )

    def get_trading_venue_instruments(self, search, type):
        load_dotenv()
        mic = os.getenv("MIC")
        response = self.client.market_data.instruments.get(mic=mic, search=search, type=type)
        print(response)


if __name__ == "__main__":
    TradingVenueInstrument().get_trading_venue_instruments("Tesla", "stock")
