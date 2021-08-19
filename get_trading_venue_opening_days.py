import os
from dotenv import load_dotenv
from helpers import RequestHandler


class TradingVenueOpeningDays(RequestHandler):
    def get_trading_venue_opening_days(self):
        load_dotenv()
        mic = os.getenv("MIC")
        endpoint = f'venues/?mic={mic}'
        response = self.get_data_data(endpoint)
        opening_days = response['results'][0].get('opening_days', None)
        print(opening_days)


if __name__ == "__main__":
    TradingVenueOpeningDays().get_trading_venue_opening_days()
