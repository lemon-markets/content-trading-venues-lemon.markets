import os
from dotenv import load_dotenv
import json


from helpers import RequestHandler, EmailSenderSendgrid


class TradingVenue(RequestHandler):
    
    def send_out_email(self):
        load_dotenv()
        endpoint = f'positions/'
        response = self.get_data_trading(endpoint)
        email_text = json.dumps(response)
        subject = "Your positions at market close"
        EmailSenderSendgrid(email_text, subject)

    def check_if_open(self):
        """
        helper function to check if the trading venue is currently open
        :return: {Boolean} is returned that tells whether trading venues is open or closed
        """
        load_dotenv()
        mic = os.getenv("MIC")
        endpoint = f'venues/?mic={mic}'
        response = self.get_data_data(endpoint)
        is_open = response['results'][0].get('is_open', 'It was not possible to retrieve the is_open attribute')
        print(is_open)
        return is_open

    def activate_order(self, order_id):
        """
        helper function to activate the order once it was placed
        :param order_id: the order ID of the order that is to be activated
        """
        load_dotenv()
        endpoint = f'orders/{order_id}/activate/'
        response = self.post_data(endpoint, {})
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
            mic = os.getenv("MIC")

            order_details = {
                "isin": "DE0008232125",  # ISIN of Lufthansa
                "expires_at": "p7d",  # specify your timestamp
                "side": "buy",
                "quantity": 1,
                "venue": mic,
            }
            endpoint = f'orders/'
            response = self.post_data(endpoint, order_details)
            order_id = response['results'].get('id', 'We were not able to retrieve the order ID.')
            # access helper function to activate the order
            self.activate_order(order_id)
            print('Order was activated')
            # additionally, we send an email with the positions at market close
            self.send_out_email()
        # throw exception in case something goes wrong
        except Exception as e:
            print('Placing order not possible', e)


if __name__ == "__main__":
    TradingVenue().place_order()
