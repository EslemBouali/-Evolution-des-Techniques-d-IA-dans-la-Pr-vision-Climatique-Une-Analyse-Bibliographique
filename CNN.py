import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np

# Génération de données fictives 
# Par exemple, 500 images climatiques de 64x64 pixels avec 3 canaux (RGB)
X_train = np.random.rand(500, 64, 64, 3)
y_train = np.random.rand(500)  # Valeurs cibles, par exemple température moyenne

# Modèle CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1)  # Prédiction d'une seule valeur (par exemple température)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Entraînement
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Exemple de prédiction
X_test = np.random.rand(10, 64, 64, 3)  # 10 nouvelles cartes climatiques
predictions = model.predict(X_test)
print("Prédictions :", predictions)
