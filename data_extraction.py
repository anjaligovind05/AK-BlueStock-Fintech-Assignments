import yfinance as yf
import pandas as pd

def fetch_market_data():
    # Tickers for Nifty 50, Reliance, TCS, and HDFC Bank
    tickers = ["^NSEI", "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
    
    print("Starting market data extraction...")
    
    # We will pull the last 5 days of data to look at recent trends
    try:
        data = yf.download(tickers, period="5d", interval="1d")
        
        # Pulling out only the closing prices
        closing_prices = data['Close']
        
        # Saving it locally to a clean CSV spreadsheet
        output_file = "market_closing_prices.csv"
        closing_prices.to_csv(output_file)
        
        print(f"Data saved successfully to {output_file}!")
        print("\nHere is a quick look at the closing data:")
        print(closing_prices.tail())
        
    except Exception as e:
        print(f"Something went wrong while pulling the data: {e}")

if __name__ == "__main__":
    fetch_market_data()
