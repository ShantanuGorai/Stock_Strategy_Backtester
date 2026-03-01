📈 Stock Strategy Backtester

A rule-based stock trading strategy simulator built using Python, Pandas, and real historical market data.

This project implements a Moving Average Crossover strategy and compares its performance against a Buy & Hold approach using backtesting.

🚀 Features

Real historical stock data using yfinance

Custom short & long moving average windows

Buy/Sell signal generation

Look-ahead bias prevention using signal shifting

Strategy vs Market comparison

Capital simulation (₹100,000 base investment)

Buy/Sell markers on price chart

Volatility calculation

🧠 Strategy Logic

The system follows a Moving Average Crossover rule:

Buy when Short MA > Long MA

Sell when Short MA < Long MA

Signals are shifted by one period to avoid look-ahead bias, ensuring realistic backtesting.

📊 Performance Metrics

The project calculates:

Market Cumulative Return

Strategy Cumulative Return

Total Profit Comparison

Last Trade Information

Current Trading Signal

🛠 Technologies Used

Python

Pandas

NumPy

Matplotlib

yfinance

▶️ How to Run

Clone the repository

Install dependencies:

pip install yfinance pandas matplotlib numpy

Run the script:

python main.py

Enter:

Stock ticker (e.g., AAPL, TSLA, RELIANCE.NS)

Start date (YYYY-MM-DD)

End date (YYYY-MM-DD)

Short & Long moving average windows

📈 Example Output

Price chart with Moving Averages

Buy/Sell markers

Strategy vs Market performance comparison

Capital growth simulation

🎯 Learning Outcomes

Through this project, I strengthened my understanding of:

Time-series analysis

Rolling window computations

Trading strategy design

Backtesting logic

Financial data processing with Pandas
