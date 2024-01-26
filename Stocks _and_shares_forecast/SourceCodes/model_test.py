import pandas as pd
import joblib
from datetime import datetime, timedelta

# Loading the saved model
model_filename = 'linear_regression_model.joblib'
loaded_model = joblib.load(model_filename)

# Reading data
df = pd.read_csv('Datasets//thy_stock_data.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# Find the last closing date
last_close_date = df.index.max()

# Finding the previous day
previous_day = last_close_date - timedelta(days=1)

# Closing price and volume of the previous day
previous_day_close = df.loc[previous_day, '4. close']
previous_day_high = df.loc[previous_day, '2. high']
previous_day_low = df.loc[previous_day, '3. low']
previous_day_volume = df.loc[previous_day, '5. volume']

# Characteristics of the next day
next_day_features = [previous_day_close, previous_day_high, previous_day_low, previous_day_volume]

# Forecasting over the model
prediction = loaded_model.predict([next_day_features])

print(f'Forecast for the next day: {prediction[0]}')
