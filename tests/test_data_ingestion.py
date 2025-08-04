"""
src/tests/test_data_ingestion.py

Purpose: Test the data ingestion functionality for fetching WTI and Brent crude oil prices.

Aim: This script tests the data ingestion functionality by mocking the EIA API response and checking if the data is correctly fetched and saved to a CSV file.
"""
import pytest 
import pandas as pd
from src.data_ingestion.fetch_wti_brent import fetch_wti_brent_prices   

#---------------------------------------------------------------------
# TestFetchWTIBrentPrices class
# This class contains pytest for the fetch_wti_brent_prices function
#---------------------------------------------------------------------

class TestFetchWTIBrentPrices:
    def test_fetch_wti_brent_prices(self, mocker):
        # Mock the requests.get method to return a predefined response
        mock_response = {
            "series": [
                {
                    "data": [
                        ["2023-01-01", 75.0],
                        ["2023-01-02", 76.0],
                        ["2023-01-03", 77.0]
                    ]
                }
            ]
        }
        mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

        # Call the function with a mock API key and output file
        api_key = 'mock_api_key'
        output_file = 'data/raw/mock_wti_brent_prices.csv'
        
        fetch_wti_brent_prices(api_key, output_file)

        # Read the saved CSV file to verify the content
        df = pd.read_csv(output_file)
        
        # Check if the DataFrame has the expected columns and data
        assert list(df.columns) == ['Date', 'WTI_Price', 'Brent_Price']
        assert len(df) == 3
        assert df['WTI_Price'].tolist() == [75.0, 76.0, 77.0]
        assert df['Brent_Price'].tolist() == [75.0, 76.0, 77.0]
        assert df['Date'].tolist() == ['2023-01-01', '2023-01-02', '2023-01-03']

        # Clean up the output file after the test
        import os
        if os.path.exists(output_file):
            os.remove(output_file)
        else: 
            fetch_wti_brent_prices(EIA_API_KEY, OUTPUT_FILE)
    
    def test_fetch_daily_ohlcv_data(self, mocker):
        # Mock the yfinance.download method to return a predefined DataFrame
        mock_data = pd.DataFrame({
            'Open': [100, 101, 102],
            'High': [105, 106, 107],
            'Low': [95, 96, 97],
            'Close': [104, 105, 106],
            'Volume': [1000, 1100, 1200]
        }, index=pd.date_range(start='2023-01-01', periods=3))

        mocker.patch('yfinance.download', return_value=mock_data)

        # Call the function with mock parameters
        tickers = ['AAPL', 'GOOGL']
        start_date = '2023-01-01'
        end_date = '2023-01-03'
        
        df = fetch_daily_ohlcv_data(tickers, start_date, end_date)

        # Check if the DataFrame has the expected columns and data
        assert list(df.columns) == ['Open', 'High', 'Low', 'Close', 'Volume']
        assert len(df) == 3
        assert df['Open'].tolist() == [100, 101, 102]
        assert df['Close'].tolist() == [104, 105, 106]

        # Clean up the mock data after the test
        del mock_data 

    