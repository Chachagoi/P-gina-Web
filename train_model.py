from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

# Datos de ejemplo
X = np.array([[20, 1], [30, 0], [40, 1], [50, 0]])
y = np.array([0, 1, 0, 1])

# Entrenamiento del modelo
model = LogisticRegression()
model.fit(X, y)

# Guardar el modelo entrenado
joblib.dump(model, 'model.pkl')

print("Modelo entrenado y guardado como 'model.pkl'")
