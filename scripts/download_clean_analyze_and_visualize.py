import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/mac/Desktop/stock-market-risk-analytics/data/downloaded_results.csv')


print("Data preview:")
print(df.head())
df['date'] = pd.to_datetime(df['date'])  
df.set_index('date', inplace=True)

# daily returns
df['daily_return'] = df['close'].pct_change()

# moving averages
df['50_day_ma'] = df['close'].rolling(window=50).mean()  # 50-day moving average
df['200_day_ma'] = df['close'].rolling(window=200).mean()  # 200-day moving average

# volatility (Annualized)
volatility = df['daily_return'].std() * (252 ** 0.5)  
print(f"Annualized Volatility: {volatility:.2%}")

# Sharpe Ratio (Annualized)
sharpe_ratio = df['daily_return'].mean() / df['daily_return'].std() * (252 ** 0.5)
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Stock Closing Price
plt.figure(figsize=(10, 6))
df['close'].plot(title="Stock Closing Price", label='Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend()
plt.show()

# Plot Stock Price and Moving Averages
plt.figure(figsize=(10, 6))
df[['close', '50_day_ma', '200_day_ma']].plot(title="Stock Price and Moving Averages", label=['Closing Price', '50-day MA', '200-day MA'])
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend()
plt.show()

# Plot Daily Returns
plt.figure(figsize=(10, 6))
df['daily_return'].plot(title="Daily Returns", label='Daily Return')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.grid(True)
plt.legend()
plt.show()

# Save the final DataFrame with calculated metrics
df.to_csv('/Users/mac/Desktop/stock-market-risk-analytics/data/final_data.csv')
