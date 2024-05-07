
class VersionSpace:
    def __init__(self, attributes):
        self.attributes = attributes
        self.space = [{} for _ in range(len(attributes))]

    def update(self, example, label):
        for i, attr in enumerate(self.attributes):
            if example[i] == label:
                self.space[i] = {h for h in self.space[i] if h[attr] == label}
            else:
                self.space[i] = {h for h in self.space[i] if h[attr] != label}

    def consistent_hypotheses(self):
        return [h for h in self.space if len(h) > 0]

class AQAlgorithm:
    def __init__(self, attributes):
        self.vs = VersionSpace(attributes)

    def train(self, examples, labels):
        for example, label in zip(examples, labels):
            self.vs.update(example, label)

    def predict(self, example):
        hypotheses = self.vs.consistent_hypotheses()
        if len(hypotheses) == 1:
            return list(hypotheses[0].values())[0]
        else:
            return None  # No se puede hacer una predicción única

# Ejemplo de uso
attributes = ['Outlook', 'Temperature', 'Humidity', 'Windy']
vs = VersionSpace(attributes)

# Ejemplos de entrenamiento
examples = [
    ('Sunny', 'Hot', 'High', 'False'),
    ('Sunny', 'Hot', 'High', 'True'),
    ('Overcast', 'Hot', 'High', 'False'),
    ('Rain', 'Mild', 'High', 'False'),
    ('Rain', 'Cool', 'Normal', 'False'),
    ('Rain', 'Cool', 'Normal', 'True'),
    ('Overcast', 'Cool', 'Normal', 'True'),
    ('Sunny', 'Mild', 'High', 'False'),
    ('Sunny', 'Cool', 'Normal', 'False'),
    ('Rain', 'Mild', 'Normal', 'False'),
]

# Etiquetas correspondientes
labels = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']

# Entrenar el modelo AQ
aq = AQAlgorithm(attributes)
aq.train(examples, labels)

# Ejemplo de predicción
example_to_predict = ('Sunny', 'Hot', 'High', 'False')
prediction = aq.predict(example_to_predict)
print("Prediction:", prediction)
