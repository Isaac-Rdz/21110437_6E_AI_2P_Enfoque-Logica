
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un clasificador de regresión logística
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Obtener la importancia de las características
feature_importance = np.abs(clf.coef_[0])
feature_importance /= feature_importance.sum()  # Normalizar

# Mostrar la importancia de las características
print("Feature Importance:")
for i, importance in enumerate(feature_importance):
    print(f"Feature {i}: {importance}")

# Ejemplo de explicación para una muestra específica
sample_index = 0
sample = X_test[sample_index]
prediction = clf.predict([sample])[0]
predicted_class = iris.target_names[prediction]
print(f"\nPredicted Class for Sample {sample_index}: {predicted_class}")

# Explicar la predicción mostrando las características más importantes
print("Explanation:")
for i, value in enumerate(sample):
    print(f"- Feature {i}: {value} (Importance: {feature_importance[i]})")
