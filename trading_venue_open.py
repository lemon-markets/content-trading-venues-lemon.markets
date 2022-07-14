import os
from dotenv import load_dotenv
import json
from lemon import api

from helpers import EmailSenderSendgrid


class TradingVenue():
    load_dotenv()

    def __init__(self):
        self.client = api.create(
            market_data_api_token=os.getenv("DATA_API_KEY"),
            trading_api_token=os.getenv("TRADING_API_KEY"),
            env="paper"
    )

    def send_out_email(self):
        response = self.client.trading.positions.get()
        email_text = json.dumps(response)
        subject = "Your positions at market close"
        EmailSenderSendgrid(email_text, subject)

    def place_order_with_email(self):
        """
        main function that places the specified order
        """
        mic = os.getenv("MIC")
        venue = self.client.market_data.venues.get(mic=mic).results[0]
        if not venue.is_open:
            email_text = "Hey there. You tried to place an order with the lemon.markets API, but the market is " \
                         "currently closed. Please try again later."
            subject = "Trade failed: the market is currently closed."
            EmailSenderSendgrid(email_text, subject)
            return

        # send notification email if trading venue is closed

        try:
            isin = "DE0008232125"  # ISIN of Lufthansa
            expires_at = 7  # specify your timestamp
            side = "buy"
            quantity = 1

            price = self.client.market_data.quotes.get_latest(isin).results[0].b
            if quantity * price < 50:
                print(f"Order price is, €{price}, which is below minimum allowed of €50.")
                return

            response = self.client.trading.orders.create(isin=isin,
                                                         quantity=quantity,
                                                         side=side,
                                                         expires_at=expires_at,
                                                         venue=mic)
            order_id = response.results.id
            self.client.trading.orders.activate(order_id=order_id)
            print('Order was activated')
            # additionally, we send an email with the positions at market close
            self.send_out_email()
        # throw exception in case something goes wrong
        except Exception as e:
            print('Placing order not possible:', e)


if __name__ == "__main__":
    TradingVenue().place_order_with_email()
