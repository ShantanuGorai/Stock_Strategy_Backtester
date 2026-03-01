import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import datetime
from datetime import date, timedelta

ticker = input("Enter stock ticker name : ")
start_date = input("Enter start date (YYYY-MM-DD) : ")
end_date = input("Enter end date (YYYY-MM-DD) : ")

stock = yf.download(ticker, start = start_date, end = end_date)

stock = stock[["Close"]].copy()
stock.dropna(inplace = True)


stock['Daily Return'] = stock['Close'].pct_change()

short_window = int(input("Enter short MA window : "))
long_window = int(input("Enter long MA window : "))

stock['MA_Short'] = stock['Close'].rolling(short_window).mean()
stock['MA_Long'] = stock['Close'].rolling(long_window).mean()

stock['Volatility'] = stock['Daily Return'].rolling(20).std()

current_vol = stock['Volatility'].iloc[-1]

if current_vol > stock['Volatility'].mean():
    print("Market is currently High Volatility")
else:
    print("Market is Stable")


stock['Signal'] = 0
stock.loc[stock['MA_Short'] > stock['MA_Long'], 'Signal'] = 1

stock['Position'] = stock['Signal'].shift(1)
stock['Position'] = stock['Position'].fillna(0)

latest_signal = stock['Position'].iloc[-1]
if latest_signal == 1:
    print("Current Signal : BUY")
else:
    print("Current Signal : SELL")

stock['Trade'] = stock['Position'].diff()
buy_signal = stock[stock['Trade'] == 1]
sell_signal = stock[stock['Trade'] == -1]

stock['Strategy Return'] = stock['Daily Return'] * stock['Position']

stock['Trade'] = stock['Position'].diff()
buy_signal = stock[stock['Trade'] == 1]
sell_signal = stock[stock['Trade'] == -1]
if not stock[stock['Trade'] != 0].empty:
    last_trade = stock[stock['Trade'] != 0].iloc[-1]
    print("Last Trade Date:", last_trade.name)
    print("Price:", round(last_trade['Close'], 2))
else:
    print("No trades executed yet.")


stock['Market Cumulative'] = (1 + stock['Daily Return']).cumprod()
stock['Strategy Cumulative'] = (1 + stock['Strategy Return']).cumprod()

initial_capital = int(input("Enter initial capital : "))
final_strategy = initial_capital * stock['Strategy Cumulative'].iloc[-1]
final_market = initial_capital * stock['Market Cumulative'].iloc[-1]

print(f"If you invested", initial_capital, " : ")
print(f"Strategy Value: ₹{round(final_strategy,2)}")
print(f"Buy & Hold Value: ₹{round(final_market,2)}")

stock['Market Value'] = initial_capital * stock['Market Cumulative']
stock['Strategy Value'] = initial_capital * stock['Strategy Cumulative']

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.plot(stock['Close'], label = 'Close')
ax1.plot(stock['MA_Short'], label = 'Short-MA')
ax1.plot(stock['MA_Long'], label = 'Long-MA')
ax1.scatter(buy_signal.index, buy_signal['Close'], marker = '^', color = 'green', s = 100, label = 'Buy')
ax1.scatter(sell_signal.index, sell_signal['Close'], marker = 'v', color = 'red', s = 100, label = 'Sell')
ax1.legend()
ax1.set_title("Price and Moving Average[MA]")

ax2.plot(stock['Daily Return'], label = 'Daily Returns', color = '#ff4d6b')
ax2.legend()
ax2.set_title("Daily Returns")

ax3.plot(stock['Volatility'], label = 'Volatility', color = '#38ce3c')
ax3.legend()
ax3.set_title("Volatility")

plt.tight_layout()
plt.show()


plt.plot(stock['Market Cumulative'], label = 'Market Cumulative', color = '#1B3A57')
plt.plot(stock['Strategy Cumulative'], label = 'Startegy Cumulative', color = '#5A5A5A')
plt.legend()
plt.title('Market Cumulative vs Strtaegy Cumulative')
plt.show()


print(stock.head())

