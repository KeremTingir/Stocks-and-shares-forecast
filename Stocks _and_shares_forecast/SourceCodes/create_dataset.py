import requests
import pandas as pd


# Alpha Vantage API key
api_key = '#####'   # Write your own API key here

# Turkish Airlines' stock symbol
symbol = 'THY'

# Pulling stock data from Alpha Vantage API
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full'
response = requests.get(url)
data = response.json()

# Converting data to DataFrame
df = pd.DataFrame(data['Time Series (Daily)']).T
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)

# ave data to CSV file
df.to_csv('DataSets//thy_stock_data.csv')

# Show the first five lines
print(df.head())
