
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import numpy as np

class M5Regressor:
    def __init__(self, max_depth=None, min_samples_split=2, min_samples_leaf=1, prune=True):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.prune = prune
        self.tree = None

    def fit(self, X, y):
        self.tree = DecisionTreeRegressor(max_depth=self.max_depth,
                                           min_samples_split=self.min_samples_split,
                                           min_samples_leaf=self.min_samples_leaf)
        self.tree.fit(X, y)

        if self.prune:
            self._prune_tree(X, y)

    def _prune_tree(self, X, y):
        if self.tree.max_depth == 1:
            return

        while True:
            n_nodes_before_prune = self.tree.tree_.node_count
            n_leaves_before_prune = np.sum(self.tree.tree_.children_left == -1)

            for i in range(n_nodes_before_prune):
                if (self.tree.tree_.children_left[i] != self.tree.tree_.children_right[i]):
                    continue

                left_child = self.tree.tree_.children_left[i]
                right_child = self.tree.tree_.children_right[i]

                if left_child == -1 or right_child == -1:
                    continue

                current_depth = np.max(self.tree.decision_path(X).todense().sum(axis=1))
                self.tree.tree_.children_left[i] = -1
                self.tree.tree_.children_right[i] = -1

                pruned_depth = np.max(self.tree.decision_path(X).todense().sum(axis=1))
                if pruned_depth < current_depth:
                    continue

                self.tree.tree_.children_left[i] = left_child
                self.tree.tree_.children_right[i] = right_child

            n_nodes_after_prune = self.tree.tree_.node_count
            n_leaves_after_prune = np.sum(self.tree.tree_.children_left == -1)

            if (n_nodes_before_prune == n_nodes_after_prune) and (n_leaves_before_prune == n_leaves_after_prune):
                break

    def predict(self, X):
        return self.tree.predict(X)

# Ejemplo de uso
import pandas as pd

# Crear un conjunto de datos de ejemplo
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 3, 4, 5, 6],
    'Target': [2, 4, 6, 8, 10]
}

df = pd.DataFrame(data)

# Separar características y objetivo
X = df[['Feature1', 'Feature2']]
y = df['Target']

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo M5
m5 = M5Regressor()
m5.fit(X_train, y_train)

# Realizar predicciones
predictions = m5.predict(X_test)
print("Predictions:", predictions)
