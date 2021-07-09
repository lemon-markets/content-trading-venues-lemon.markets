from helpers import RequestHandler


class TradingVenues(RequestHandler):
    def get_all_trading_venues(self):
        endpoint = 'trading-venues/'
        response = self.get_data(endpoint)
        print(response)


if __name__ == "__main__":
    TradingVenues().get_all_trading_venues()
