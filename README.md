# Emabacktester

This repository contains a Python-based backtesting framework for the Exponential Moving Average (EMA) crossover strategy using historical stock data via yfinance. It evaluates performance against a buy-and-hold benchmark and provides metrics like total return, risk, and Sharpe ratio

🚀 Features :

- Fetches historical stock data via yfinance
- Implements a simple EMA crossover strategy
- Computes:
   - Log returns
   - Cumulative strategy returns
   - Buy & Hold returns
   - Sharpe Ratio
   - Total Return & Risk
   - Outperformance ratio
Visualizes strategy vs. benchmark
Modular and object-oriented design

🧠 How It Works:

- Two EMAs are calculated (short-term and long-term).
- A position is taken: 1 (long) when short EMA > long EMA, else -1 (short).
- Strategy returns are based on log returns adjusted by the position.
- The results are compared with buy-and-hold strategy performance.


# Quick Example
bt = EMAbacktester("AAPL", "2020-01-01", "2023-01-01", EMA_1=20, EMA_2=50)
bt.test_results()
bt.plot_results()


**🤝 License**

MIT License. Free to use and modify.
