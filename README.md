# lemon.markets Trading Venues

This is a public [lemon.markets](https://lemon.markets) repository that outlines a number of use cases for our trading venue endpoints. If you're not yet part of lemon.markets, be sure to sign up for our [waitlist](https://www.lemon.markets/waitlist).

## What to do with it?

We included a number of Python scripts that are supposed to help you get started with our trading venue endpoints. 
You will have to make a few changes within the script to make them work. 
- insert an access token at the sections marked with **"YOUR-TOKEN-HERE"**;
- specifiy your trading venue using the **Market Identifier Code (mic)** (we currently support the Munich Stock Exchange (**XMUN**) but watch out for additional ones in the future;
- include the proper URL in the requests.

## What use cases are covered by this repo?
The Python scripts deal with different endpoints concerned with the topic of trading venues. Specifically:
- **get_single_trading_venue.py**: retrieve a specific trading venue using its Market Identifier Code (MIC)
- **get_trading_venue_instrument.py**: search for instruments traded on a specific trading venue
- **get_trading_venue_opening_days.py**: get an array of all opening days including opening and closing times of a specific trading venue
- **trading_venues.py**: get a list of all trading venues on lemon.markets
- **trading_venue_open.py**: a small script that checks whether a trading venue is currently open. If it is, an order is placed. If it is not, the user receives an email notifying him:her that the market is closed. Additionally, the script sends an automatic email at market close notifying the user of his:her portfolio.

## Sending Emails
In this repo, we are using the Sendgrid API to send emails. You need a Sendgrid API Key, which you can pass as an environment variable. If you do not have a Sendgrid Account, yet: sign up [here](https://sendgrid.com/)

## Environment Variables
In order to be able to use the script, please set the following environment variables:
- API_KEY = "Your lemon.markets API key"
- BASE_URL_TRADING = "The base URL of our Paper Trading API"
- BASE_URL_DATA = "The base URL of our Market Data API"
- MIC = "Market Identifier Code of Trading Venue"
- SENDGRID_API_KEY = "Your Sendgrid API Key"
- EMAIL_FROM = "Email you want to send emails from"
- EMAIL_TO="Email you want to send emails to"

## Interested in contributing?

This (and all lemon.markets open source projects) is work in progress. If you are interested in contributing to this repo, simply create a PR and/or contact us at [support@lemon.markets](mailto:support@lemon.markets). 

Looking forward to building lemon.markets with you 🍋

