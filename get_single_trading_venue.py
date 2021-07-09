import os
from dotenv import load_dotenv
from helpers import RequestHandler


class SingleTradingVenue(RequestHandler):
    def get_single_trading_venue(self):
        load_dotenv()
        mic = os.getenv("MIC")
        endpoint = f'trading-venues/{mic}'
        response = self.get_data(endpoint)
        print(response)


if __name__ == "__main__":
    SingleTradingVenue().get_single_trading_venue()

