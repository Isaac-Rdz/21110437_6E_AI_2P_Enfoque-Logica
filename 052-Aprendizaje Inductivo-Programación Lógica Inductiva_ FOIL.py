
class FOIL:
    def __init__(self, positive_examples, negative_examples, target_predicate):
        self.positive_examples = positive_examples
        self.negative_examples = negative_examples
        self.target_predicate = target_predicate
        self.clauses = []

    def learn(self):
        for pos_example in self.positive_examples:
            self.clauses.append(self.learn_clause(pos_example))

    def learn_clause(self, pos_example):
        clause = ""
        for i, val in enumerate(pos_example[:-1]):
            clause += f"{self.target_predicate}{i}={val}, "
        clause += f"=> {self.target_predicate}={pos_example[-1]}"
        return clause

# Ejemplo de uso
positive_examples = [
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1)
]

negative_examples = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0)
]

target_predicate = "Target"

foil = FOIL(positive_examples, negative_examples, target_predicate)
foil.learn()

print("Learned Clauses:")
for clause in foil.clauses:
    print(clause)
