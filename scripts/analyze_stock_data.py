import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/mac/Desktop/stock-market-risk-analytics/data/processed/AAPL_cleaned.csv')
print("Columns in AAPL data:", df.columns)
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

df = df.dropna(subset=['Close'])
start_date = '2022-01-01' 
num_days = len(df)  
dates = pd.date_range(start=start_date, periods=num_days, freq='B')  

df['Date'] = dates
df.set_index('Date', inplace=True)

print(df.head())

# Plot closing price
df['Close'].plot(title='AAPL Closing Price', figsize=(10, 5))
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid()
plt.show()

df['Daily Return'] = df['Close'].pct_change() 
volatility = df['Daily Return'].std() * np.sqrt(252)  
print(f"AAPL Volatility: {volatility:.2%}")

sharpe = df['Daily Return'].mean() / df['Daily Return'].std() * np.sqrt(252)
print(f"AAPL Sharpe Ratio: {sharpe:.2f}")

df['Cumulative Return'] = (1 + df['Daily Return']).cumprod()

df[['Daily Return', 'Cumulative Return']].plot(subplots=True, figsize=(12, 6))
plt.show()

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

combined_df = pd.DataFrame()

for ticker in tickers:
    data = pd.read_csv(f'/Users/mac/Desktop/stock-market-risk-analytics/data/processed/{ticker}_cleaned.csv')

    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
    data = data.dropna(subset=['Close'])  

    num_days = len(data)
    dates = pd.date_range(start=start_date, periods=num_days, freq='B')
    data['Date'] = dates
    data.set_index('Date', inplace=True)

    combined_df[ticker] = data['Close']

combined_df.plot(figsize=(12, 6), title='Stock Prices Comparison')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid()
plt.show()

