from binance.client import Client
import logging

# Correct logging setup
logging.basicConfig(
    filename='log.txt',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logging.info("Test Log - Bot Initialized Successfully")

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi'
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

        print("[INFO] Trading Bot Initialized (Testnet Mode)")
        logging.info("Trading Bot Initialized in Testnet Mode")

    def place_market_order(self, symbol, side, quantity):
        try:
            print(f"[INFO] Placing Market Order: {side} {quantity} {symbol}")
            logging.info(f"Placing Market Order: {side} {quantity} {symbol}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            logging.info(f'Market Order Response: {order}')
            print("[SUCCESS] Market Order Placed. Check log.txt for details.")
            return order

        except Exception as e:
            logging.error(f'Error placing market order: {e}')
            print(f"[ERROR] Market Order Failed: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            print(f"[INFO] Placing Limit Order: {side} {quantity} {symbol} at {price}")
            logging.info(f"Placing Limit Order: {side} {quantity} {symbol} at {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logging.info(f'Limit Order Response: {order}')
            print("[SUCCESS] Limit Order Placed. Check log.txt for details.")
            return order

        except Exception as e:
            logging.error(f'Error placing limit order: {e}')
            print(f"[ERROR] Limit Order Failed: {e}")
            return None
