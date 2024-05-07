
import numpy as np

class Node:
    def __init__(self, attribute=None, label=None):
        self.attribute = attribute  # Atributo en base al cual se divide el árbol
        self.label = label  # Etiqueta si es un nodo hoja
        self.children = {}  # Diccionario de hijos (valor del atributo -> nodo)

def entropy(class_labels):
    _, counts = np.unique(class_labels, return_counts=True)
    probabilities = counts / len(class_labels)
    return -np.sum(probabilities * np.log2(probabilities))

def information_gain(data, target, attribute):
    # Entropía del conjunto total
    total_entropy = entropy(target)

    # Entropía después de dividir según el atributo
    weighted_entropy = 0
    _, counts = np.unique(data[attribute], return_counts=True)
    for value, count in zip(data[attribute].unique(), counts):
        subset_target = target[data[attribute] == value]
        weighted_entropy += (count / len(data)) * entropy(subset_target)

    # Ganancia de información
    return total_entropy - weighted_entropy

def id3(data, target, attributes):
    # Caso base: todos los ejemplos tienen la misma etiqueta
    if len(np.unique(target)) == 1:
        return Node(label=target.iloc[0])

    # Caso base: no quedan atributos para dividir
    if len(attributes) == 0:
        return Node(label=target.value_counts().idxmax())

    # Seleccionar el mejor atributo según la ganancia de información
    best_attribute = max(attributes, key=lambda a: information_gain(data, target, a))

    # Crear nodo con el mejor atributo
    node = Node(attribute=best_attribute)

    # Recursión para cada valor del atributo
    for value in data[best_attribute].unique():
        subset_data = data[data[best_attribute] == value]
        subset_target = target[data[best_attribute] == value]
        if len(subset_data) == 0:
            node.children[value] = Node(label=target.value_counts().idxmax())
        else:
            node.children[value] = id3(subset_data, subset_target, attributes - {best_attribute})

    return node

def predict(tree, sample):
    if tree.label is not None:
        return tree.label
    else:
        attribute_value = sample[tree.attribute]
        if attribute_value not in tree.children:
            return None  # Valor no visto durante el entrenamiento
        else:
            return predict(tree.children[attribute_value], sample)

# Ejemplo de uso
import pandas as pd

# Dataset de ejemplo (Outlook, Temperature, Humidity, Windy)
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal'],
    'Windy': ['False', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'False', 'False'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Separar atributos y etiquetas
X = df.drop(columns=['PlayTennis'])
y = df['PlayTennis']

# Entrenar el árbol de decisión
attributes = set(X.columns)
tree = id3(X, y, attributes)

# Predicción de un nuevo ejemplo
sample = {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'False'}
prediction = predict(tree, sample)
print("Prediction:", prediction)
