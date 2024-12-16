import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Exemple de données
import numpy as np
data = np.sin(np.linspace(0, 100, 1000)).reshape(-1, 10, 1)

# Définir un modèle LSTM
model = Sequential([
    LSTM(50, activation='relu', input_shape=(10, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Entraîner
model.fit(data, data[:, -1, :], epochs=10)
