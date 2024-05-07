
from grammar_induction import create_possible_rules, create_grammar, expand

# Ejemplos de secuencias de palabras
sequences = [
    ['the', 'cat', 'saw', 'a', 'dog'],
    ['a', 'dog', 'chased', 'the', 'cat'],
    ['the', 'cat', 'chased', 'the', 'mouse']
]

# Crear posibles reglas de producción
rules = create_possible_rules(sequences)

# Crear la gramática a partir de las reglas
grammar = create_grammar(rules)

# Expandir la gramática para generar nuevas secuencias
expanded_sequences = expand(grammar, max_length=10)

# Mostrar la gramática y las nuevas secuencias generadas
print("Gramática:")
print(grammar)
print("\nNuevas secuencias generadas:")
for sequence in expanded_sequences:
    print(sequence)
