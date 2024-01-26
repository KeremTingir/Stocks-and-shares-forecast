import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading data
df = pd.read_csv('Datasets//thy_stock_data.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# Select data within a specific date range (for example, data between 2020-06-25 and 2024-01-25)
start_date = '2020-06-25'
end_date = '2024-01-25'
selected_data = df[start_date:end_date]

# Create a line graph
plt.figure(figsize=(12, 6))
sns.lineplot(x=selected_data.index, y=selected_data['4. close'], marker='o', color='b')
plt.title('Turkish Airlines Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()
