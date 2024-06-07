import requests
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'YOUR_API_KEY' with your actual Polygon.io API key
api_key = '2X7uQpLKJtu2ITWK2tTdoS5DTJPANOEN'
ticker = 'INTC'

# Construct the API URL for daily historical data
url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2024-03-18/2024-03-30?apiKey={api_key}'

# Make the request
response = requests.get(url)
data = response.json()

# Check if the API call was successful
if response.status_code == 200 and 'results' in data:

    # Extract the relevant data
    dates = [entry['t'] for entry in data['results']]
    closes = [entry['c'] for entry in data['results']]

    # Convert timestamps to datetime objects and create a DataFrame
    dates = pd.to_datetime(dates, unit='ms')
    df = pd.DataFrame({'Close': closes}, index=dates)

    # Assuming df is your DataFrame and it has a 'Close' column
    df['26-day EMA'] = df['Close'].ewm(span=26, adjust=False).mean()
    df['12-day EMA'] = df['Close'].ewm(span=12, adjust=False).mean()

    # Calculate the difference between the 26-day EMA and the 12-day EMA
    df['EMA Difference'] = df['12-day EMA'] - df['26-day EMA']
    # Calculate the 9-day EMA of the MACD line (Signal Line)
    df['Signal Line'] = df['EMA Difference'].ewm(span=9, adjust=False).mean()

    # Calculate the MACD Histogram
    df['MACD Histogram'] = df['EMA Difference'] - df['Signal Line']
    # Assuming you have the MACD line as 'EMA Difference' and the Signal line already calculated in your DataFrame `df`

    # Find crossings
    crossings = df['EMA Difference'] - df['Signal Line']
    crossings_previous = crossings.shift(1)
    crosses_above = (crossings > 0) & (crossings_previous < 0)
    crosses_below = (crossings < 0) & (crossings_previous > 0)

    # Buy signals - when MACD crosses above the signal line
    buy_signals = df[crosses_above]

    # Sell signals - when MACD crosses below the signal line
    sell_signals = df[crosses_below]


    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['EMA Difference'], label='MACD Line')
    plt.plot(df.index, df['Signal Line'], label='Signal Line', color='orange')
    plt.scatter(buy_signals.index, buy_signals['EMA Difference'], color='green', marker='^', alpha=1, label='Buy Signal')
    plt.scatter(sell_signals.index, sell_signals['EMA Difference'], color='red', marker='v', alpha=1, label='Sell Signal')
    plt.axhline(y = 0.0, color = 'grey', linestyle = '-')
    plt.bar(df.index, df['MACD Histogram'], label='MACD Histogram', color='grey', alpha=0.5)
    plt.title('MACD Indicator for Apple')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


else:
    
    print("Failed to fetch data:", data.get('error', 'Unknown error'))