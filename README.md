# 📈 StockTrader: MACD Buy/Sell Signal Analyzer

**StockTrader** is a Python script that analyzes historical stock price data using the MACD (Moving Average Convergence Divergence) indicator to generate **buy** and **sell** signals. It evaluates the accuracy of each type of signal and visualizes them using `matplotlib`. Data is fetched from the [Polygon.io API](https://polygon.io/), and signals are calculated and plotted for any selected stock ticker.

> ✨ Example: Analyze MACD strategy for **NFLX** between March 18–30, 2024.

---

## 🔍 What It Does

- Pulls historical daily price data from Polygon.io
- Calculates:
  - 12-day and 26-day exponential moving averages (EMAs)
  - MACD line
  - Signal line (9-day EMA of MACD)
  - MACD histogram
- Detects:
  - **Buy signals** (MACD crossing above signal line)
  - **Sell signals** (MACD crossing below signal line)
- Computes the **average accuracy** of buy/sell signals over a 5-day future window
- Displays a clean **matplotlib plot** with all indicators and signals

---

## 📦 Requirements

Install the required libraries using:

```bash
pip install pandas numpy matplotlib requests
```
