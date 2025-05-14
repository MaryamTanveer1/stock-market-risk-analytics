import yfinance as yf
import pandas as pd
import os


os.makedirs('../data/raw', exist_ok=True)
os.makedirs('../data/processed', exist_ok=True)
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
start_date = '2022-01-01'
end_date = '2024-12-31'
for ticker in tickers:
    print(f"Fetching data for {ticker}")
    df = yf.download(ticker, start=start_date, end=end_date)
    raw_path = f"../data/raw/{ticker}.csv"
    df.to_csv(raw_path)
    df.dropna(inplace=True)  
    df = df[df['Volume'] > 0]  
    clean_path = f"../data/processed/{ticker}_cleaned.csv"
    df.to_csv(clean_path)
    print(f"Saved cleaned data for {ticker}")
