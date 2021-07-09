import os
from dotenv import load_dotenv
import json
import time

from helpers import RequestHandler, EmailSenderSendgrid


class TradingVenue(RequestHandler):
    def get_closing_time(self):
        """
        helper function to get next closing time
        :return: {int} the timestamp close is returned
        """
        load_dotenv()
        mic = os.getenv("MIC")
        endpoint = f'trading-venues/{mic}/opening-days/'
        response = self.get_data(endpoint)
        timestamp_close = response['results'][0].get('closing_time', None)
        print(timestamp_close)
        return timestamp_close

    def get_portfolio(self):
        """
        helper function to get the space's portfolio
        """
        load_dotenv()
        space_uuid = os.getenv("SPACE_UUID")
        endpoint = f'spaces/{space_uuid}/portfolio/'
        response = self.get_data(endpoint)
        email_text = json.dumps(response)
        subject = "Your Portfolio at market close"
        EmailSenderSendgrid(email_text, subject)

    def send_out_close_email(self):
        """
        helper function to determine the time until market close
        """
        # get the current time
        current_time = time.time()
        # sleep until market close
        print(f'Waiting for {(self.get_closing_time()-current_time)/60/60} hours')
        time.sleep(self.get_closing_time()-current_time)
        # get the portfolio at market close and send out email
        self.get_portfolio()

    def check_if_open(self):
        """
        helper function to check if the trading venue is currently open
        :return: {Boolean} is returned that tells whether trading venues is open or closed
        """
        load_dotenv()
        mic = os.getenv("MIC")
        endpoint = f'trading-venues/{mic}'
        response = self.get_data(endpoint)
        is_open = response.get('is_open', 'It was not possible to retrieve the is_open attribute')
        print(is_open)
        return is_open

    def activate_order(self, order_uuid):
        """
        helper function to activate the order once it was placed
        :param order_uuid: the order UUID of the order that is to be activated
        """
        load_dotenv()
        space_uuid = os.getenv("SPACE_UUID")
        endpoint = f'spaces/{space_uuid}/orders/{order_uuid}/activate/'
        response = self.put_data(endpoint)
        print(response)

    def place_order(self):
        """
        main function that places the specified order
        """
        load_dotenv()
        if not self.check_if_open():
            email_text = "Hey there. You tried to place an order with the lemon.markets API, but the market is currently closed. Please try again later."
            subject = "The market is currently closed"
            EmailSenderSendgrid(email_text, subject)
            return

        # send notification email if trading venue is closed
        try:
            order_details = {
                "isin": "DE0008232125",  # ISIN of Lufthansa
                "valid_until": 2000000000,  # specify your timestamp
                "side": "buy",
                "quantity": 1,
            }
            space_uuid = os.getenv("SPACE_UUID")
            endpoint = f'spaces/{space_uuid}/orders/'
            response = self.post_data(endpoint, order_details)
            order_uuid = response.get('uuid')
            # access helper function to activate the order
            self.activate_order(order_uuid)
            print('order was activated')
            # additionally, we send an email with the portfolio items at market close
            self.send_out_close_email()
        # throw exception in case something goes wrong
        except Exception as e:
            print('placing order not possible', e)


if __name__ == "__main__":
    TradingVenue().place_order()
