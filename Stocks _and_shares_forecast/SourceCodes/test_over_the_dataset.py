import pandas as pd
import joblib
from datetime import datetime, timedelta
import random

# Loading the saved model
model_filename = 'linear_regression_model.joblib'
loaded_model = joblib.load(model_filename)

# Reading data
df = pd.read_csv('Datasets//thy_stock_data.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# Selecting test data
test_data = df.sample(n=1, random_state=random.seed())  # Rastgele bir gün seç

# Characteristics of the selected day
selected_day = test_data.index[0]
selected_day_close = test_data.loc[selected_day, '4. close']
selected_day_high = test_data.loc[selected_day, '2. high']
selected_day_low = test_data.loc[selected_day, '3. low']
selected_day_volume = test_data.loc[selected_day, '5. volume']

# Find the realized closing price of the next day
next_day = selected_day + timedelta(days=1)
next_day_close = df.loc[next_day, '4. close']

# Forecasting over the model
prediction = loaded_model.predict([[selected_day_close, selected_day_high, selected_day_low, selected_day_volume]])

# Comparison of forecast and realized value
print(f'Selected day {selected_day}')
print(f'Actual closing price: {next_day_close}')
print(f'Estimated closing price of the model: {prediction[0]}')
