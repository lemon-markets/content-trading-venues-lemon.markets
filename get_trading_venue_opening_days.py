import os
from dotenv import load_dotenv
from helpers import RequestHandler


class TradingVenueOpeningDays(RequestHandler):
    def get_trading_venue_opening_days(self):
        load_dotenv()
        mic = os.getenv("MIC")
        endpoint = f'trading-venues/{mic}/opening-days'
        response = self.get_data(endpoint)
        print(response)


if __name__ == "__main__":
    TradingVenueOpeningDays().get_trading_venue_opening_days()
