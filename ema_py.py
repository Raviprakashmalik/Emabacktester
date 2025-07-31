

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random



class EMAbacktester():
    def __init__(self,symbol,start,end,EMA_1,EMA_2):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.EMA_1 = EMA_1
        self.EMA_2 = EMA_2
        self.results = None
        self.get_data()

    def get_data(self):
        tick = yf.download(self.symbol, start=self.start, end=self.end)
        tick["EMA_1"] = tick.Close.ewm(span=self.EMA_1).mean()
        tick["EMA_2"] =tick.Close.ewm(span=self.EMA_2).mean()
        tick.dropna(inplace=True)
        self.data = tick

        return tick

    def test_results(self):
        data = self.data.copy().dropna()
        data["position"] = np.where(data["EMA_1"] > data["EMA_2"], 1,-1)
        data["d_returns"] = np.log(data["Close"].div(data["Close"].shift(1)))
        data["d_strategy_returns"] = data["d_returns"] * data["position"].shift(1)
        data.dropna(inplace=True)
        data["buy&hold_returns"] = np.exp(data["d_returns"].cumsum())
        data["cum_strategy_returns"] = np.exp(data["d_strategy_returns"].cumsum())
        performance = data["cum_strategy_returns"].iloc[-1]
        outperformance = performance / data["buy&hold_returns"].iloc[-1]
        self.results = data
        returns = data["d_strategy_returns"].sum()
        risk = data["d_strategy_returns"].std() * np.sqrt(252)
        sharpe = (data["d_strategy_returns"].mean() / data["d_strategy_returns"].std()) * np.sqrt(252)

        return {
            "performance": round(performance, 5),
            "outperformance": round(outperformance, 5),
            "total_return": returns,
            "risk": risk,
            "sharpe": sharpe}



    def plot_results(self):
        if self.results is None:
            print("Run the test please")
        else:
            title="{}| EMA_1={} | EMA_2={}".format(self.symbol,self.EMA_1, self.EMA_2)
            self.results[["buy&hold_returns","d_strategy_returns"]].plot(title=title, figsize=(12,8))

