# Linear Regression - Day 5 Practice

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

 
X = [[1000], [1200], [1500], [1800], [2000], [2500], [3000]]
y = [200, 240, 300, 360, 400, 500, 600]

 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

 
model = LinearRegression()
model.fit(X_train, y_train)

 
y_pred = model.predict(X_test)

 
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

 
print("Test Data:", X_test)
print("Actual Values:", y_test)
print("Predicted Values:", y_pred)

print("\nModel Performance:")
print("MAE:", mae)
print("RMSE:", rmse)

 
sample_house = [[1600]]
prediction = model.predict(sample_house)

print("\nPrediction for 1600 sqft house:", prediction[0])