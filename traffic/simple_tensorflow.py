#This is a simple test of tensorflow that was created with GPT3

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Sample data
# Replace this with your actual dataset
# For demonstration, we'll use a simple linear relationship: y = 2x + 1
np.random.seed(42)
num_train=100
X_train = np.random.rand(num_train, 1)
y_train = 2 * X_train + 1 + 0.1 * np.random.randn(num_train, 1)

# Define a simple neural network
model = Sequential()
model.add(Dense(units=1, input_dim=1, activation='linear'))

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=50, verbose=1)

# Evaluate the trained model
X_test = np.array([[0.2], [0.5], [0.8]])
predictions = model.predict(X_test)

# Print the predictions
for i in range(len(X_test)):
    print(f"Input: {X_test[i][0]}, Predicted Output: {predictions[i][0]}")
