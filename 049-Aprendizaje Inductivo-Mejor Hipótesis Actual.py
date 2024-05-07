
import numpy as np

class BestCurrentHypothesis:
    def __init__(self, num_features):
        self.num_features = num_features
        self.weights = np.zeros(num_features + 1)  # +1 para el término de sesgo
        self.loss = float('inf')  # Pérdida inicialmente infinita

    def fit(self, X, y):
        # Agregar una columna de unos para el término de sesgo
        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)

        # Actualizar los pesos utilizando el descenso de gradiente
        learning_rate = 0.01
        num_iterations = 1000
        for _ in range(num_iterations):
            predictions = np.dot(X, self.weights)
            error = predictions - y
            gradient = np.dot(X.T, error) / len(y)
            self.weights -= learning_rate * gradient

            # Calcular la pérdida
            current_loss = np.mean((predictions - y) ** 2)
            if current_loss < self.loss:
                self.loss = current_loss
            else:
                break  # Detener el entrenamiento si la pérdida comienza a aumentar

    def predict(self, X):
        # Agregar una columna de unos para el término de sesgo
        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
        return np.dot(X, self.weights[1:]) + self.weights[0]  # Ajustar el término de sesgo

# Ejemplo de uso
# Generar datos de ejemplo
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Inicializar y entrenar la hipótesis actual
bch = BestCurrentHypothesis(num_features=1)
bch.fit(X, y)

# Realizar predicciones
X_new = np.array([[0], [2]])
predictions = bch.predict(X_new)
print("Predictions:", predictions)
