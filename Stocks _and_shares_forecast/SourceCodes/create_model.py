import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Reading data
df = pd.read_csv('Datasets//thy_stock_data.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# Feature and target selection
features = ['1. open', '2. high', '3. low', '5. volume']
target = '4. close'

X = df[features]
y = df[target]

# Dividing data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Saving the model
model_filename = 'linear_regression_model.joblib'
joblib.dump(model, model_filename)
print(f'Model recorded: {model_filename}')

# Evaluation of the model on the test set
y_pred = model.predict(X_test)

# Create a new DataFrame with actual and predicted values
comparison_df = pd.DataFrame({'Actual Value': y_test, 'Estimated Value': y_pred})

# Create a new DataFrame with actual and predicted values
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Actual Value', y='Estimated Value', data=comparison_df)
plt.title('Actual Value vs. Estimated Value')
plt.xlabel('Actual Value')
plt.ylabel('Estimated Value')
plt.show()
