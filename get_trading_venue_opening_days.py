import os
from dotenv import load_dotenv
from lemon import api


class TradingVenueOpeningDays:

    def __init__(self):
        load_dotenv()
        self.client = api.create(
            market_data_api_token=os.getenv("DATA_API_KEY"),
            trading_api_token=os.getenv("TRADING_API_KEY"),
            env="paper"
    )

    def get_trading_venue_opening_days(self):
        load_dotenv()
        mic = os.getenv("MIC")
        response = self.client.market_data.venues.get(mic)
        opening_days = response.results[0].opening_days
        print(opening_days)


if __name__ == "__main__":
    TradingVenueOpeningDays().get_trading_venue_opening_days()
