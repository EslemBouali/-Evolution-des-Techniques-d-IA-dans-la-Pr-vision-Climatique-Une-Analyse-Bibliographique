import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

# Génération de données fictives 
# 500 séquences temporelles, chacune avec 30 pas de temps et 1 variable (température)
X_train = np.random.rand(500, 30, 1)
y_train = np.random.rand(500)  # Valeur cible (par exemple température à t+1)

# Modèle LSTM
model = Sequential([
    LSTM(50, activation='relu', input_shape=(30, 1)),
    Dense(1)  # Prédiction d'une seule valeur (température future)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Entraînement
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Exemple de prédiction
X_test = np.random.rand(10, 30, 1)  # 10 nouvelles séries temporelles
predictions = model.predict(X_test)
print("Prédictions :", predictions)
