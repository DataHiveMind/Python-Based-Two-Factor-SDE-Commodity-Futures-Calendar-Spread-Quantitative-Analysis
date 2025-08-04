"""
src/data_ingestion/fetch_wti_brent.py

Purpose: Fetch WTI and Brent crude oil prices from the EIA API.

Aim: This script fetches the latest WTI and Brent crude oil prices, and daily OHLCV data for 200 US large-caps from the EIA API and saves them to a CSV file and place them into the data/raw folder.

"""
import requests
import yfinance as yf
import pandas as pd

#---------------------------------------------------------------------
# fetch_wti_brent_prices function
# function to fetch WTI and Brent crude oil prices from the EIA API
#---------------------------------------------------------------------

def fetch_wti_brent_prices(api_key: str, output_file: str) -> None:
    """
    Fetch WTI and Brent crude oil prices from the EIA API and save to a CSV file.

    Parameters:
    - api_key (str): Your EIA API key.
    - output_file (str): Path to the output CSV file.
    """
    base_url = "https://api.eia.gov/series/"
    
    # Define series IDs for WTI and Brent
    series_ids = {
        "WTI": "PET.RWTC.D",
        "Brent": "PET.RBRTD.D"
    }
    
    data = {}
    
    for name, series_id in series_ids.items():
        response = requests.get(base_url, params={"api_key": api_key, "series_id": series_id})
        response.raise_for_status()  # Raise an error for bad responses
        data[name] = response.json()['series'][0]['data']
    
    # Convert to DataFrame
    df_wti = pd.DataFrame(data['WTI'], columns=['Date', 'WTI_Price'])
    df_brent = pd.DataFrame(data['Brent'], columns=['Date', 'Brent_Price'])
    
    # Merge DataFrames on Date
    df = pd.merge(df_wti, df_brent, on='Date')
    
    # Save to CSV
    df.to_csv(output_file, index=False)

def fetch_daily_ohlcv_data(tickers: list, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch daily OHLCV data for a list of tickers from Yahoo Finance.

    Parameters:
    - tickers (list): List of stock tickers.
    - start_date (str): Start date in 'YYYY-MM-DD' format.
    - end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
    - pd.DataFrame: DataFrame containing OHLCV data.
    """
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

#---------------------------------------------------------------------
# Example usage
#---------------------------------------------------------------------
if __name__ == "__main__":
    import os
    
    # Set your EIA API key and output file path
    EIA_API_KEY = os.getenv('EIA_API_KEY', 'your_api_key_here')  # Replace with your actual API key
    OUTPUT_FILE = 'data/raw/wti_brent_prices.csv'

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Fetch and save WTI and Brent prices
    fetch_wti_brent_prices(EIA_API_KEY, OUTPUT_FILE)
    print(f"WTI and Brent prices saved to {OUTPUT_FILE}")
    print("Data fetching complete.")

    # Example tickers for daily OHLCV data
    example_tickers = ['AAPL', 'MSFT', 'GOOGL']
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    # Fetch daily OHLCV data for example tickers
    daily_ohlcv_data = fetch_daily_ohlcv_data(example_tickers, start_date, end_date)
    
    # Save the daily OHLCV data to a CSV file
    daily_ohlcv_file = 'data/raw/daily_ohlcv_data.csv'
    daily_ohlcv_data.to_csv(daily_ohlcv_file)
