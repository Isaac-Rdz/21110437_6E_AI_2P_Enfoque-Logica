
class ReasoningAndLearning:
    def __init__(self):
        pass

    def deductive_reasoning(self, statement):
        if "Socrates" in statement and "man" in statement:
            return "Socrates is a man, therefore he is mortal."
        else:
            return "I cannot deduce anything from this statement."

    def inductive_reasoning(self, data):
        if all(x > 0 for x in data):
            return "All the numbers in the dataset are positive."
        else:
            return "Not all the numbers in the dataset are positive."

    def abductive_reasoning(self, observation):
        if observation == "The grass is wet":
            return "It rained."
        else:
            return "I don't have enough information to make an inference."

    def supervised_learning(self, dataset):
        # Dummy example: predict whether a number is even or odd
        predictions = []
        for number in dataset:
            if number % 2 == 0:
                predictions.append("even")
            else:
                predictions.append("odd")
        return predictions

    def unsupervised_learning(self, dataset):
        # Dummy example: clustering numbers into two groups
        cluster1 = []
        cluster2 = []
        for number in dataset:
            if number > 5:
                cluster1.append(number)
            else:
                cluster2.append(number)
        return cluster1, cluster2

# Ejemplo de uso
reasoner = ReasoningAndLearning()

# Razonamiento deductivo
deductive_result = reasoner.deductive_reasoning("Socrates is a man")
print("Deductive Reasoning:", deductive_result)

# Razonamiento inductivo
inductive_result = reasoner.inductive_reasoning([1, 2, 3])
print("Inductive Reasoning:", inductive_result)

# Razonamiento abductivo
abductive_result = reasoner.abductive_reasoning("The grass is wet")
print("Abductive Reasoning:", abductive_result)

# Aprendizaje supervisado
supervised_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
supervised_result = reasoner.supervised_learning(supervised_data)
print("Supervised Learning Predictions:", supervised_result)

# Aprendizaje no supervisado
unsupervised_result = reasoner.unsupervised_learning(supervised_data)
print("Unsupervised Learning Clusters:", unsupervised_result)
