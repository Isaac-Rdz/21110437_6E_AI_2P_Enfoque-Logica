
class Grammar:
    def __init__(self, rules):
        self.rules = rules

    def generate(self, symbol):
        if symbol in self.rules:
            return self.rules[symbol]
        else:
            return [symbol]

# Definir reglas para cada tipo de gramática
type_0_rules = {
    'S': ['AB', 'BA'],
    'A': ['aA', 'a', ''],
    'B': ['bB', 'b', '']
}

type_1_rules = {
    'AB': ['BC', 'B']
}

type_2_rules = {
    'A': ['xB', 'x'],
    'B': ['y']
}

type_3_rules = {
    'A': ['x']
}

# Crear gramáticas para cada tipo
type_0_grammar = Grammar(type_0_rules)
type_1_grammar = Grammar(type_1_rules)
type_2_grammar = Grammar(type_2_rules)
type_3_grammar = Grammar(type_3_rules)

# Generar secuencias para cada tipo de gramática
print("Tipo 0:")
print(type_0_grammar.generate('S'))

print("\nTipo 1:")
print(type_1_grammar.generate('AB'))

print("\nTipo 2:")
print(type_2_grammar.generate('A'))

print("\nTipo 3:")
print(type_3_grammar.generate('A'))
