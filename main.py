import os
from dotenv import load_dotenv
from bot import BasicBot

# Load API keys from .env file
load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

if not api_key or not api_secret:
    print("[ERROR] API Key or Secret not set in .env file.")
    exit()

# Initialize the Trading Bot
bot = BasicBot(api_key, api_secret)

print("\n🚀 Welcome to Binance Futures Trading Bot (Testnet)\n")

while True:
    print("\nSelect Order Type:")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == '1':
        symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper().strip()
        side = input("Enter Side (BUY/SELL): ").upper().strip()
        quantity = float(input("Enter Quantity: ").strip())
        
        result = bot.place_market_order(symbol, side, quantity)
        print("Order Result:", result)

    elif choice == '2':
        symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper().strip()
        side = input("Enter Side (BUY/SELL): ").upper().strip()
        quantity = float(input("Enter Quantity: ").strip())
        price = float(input("Enter Limit Price: ").strip())
        
        result = bot.place_limit_order(symbol, side, quantity, price)
        print("Order Result:", result)

    elif choice == '3':
        print("Exiting Trading Bot. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice, please select 1, 2, or 3.")
