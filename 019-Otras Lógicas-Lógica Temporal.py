
from tempura import Temporal, parse
from tempura.semantics import KripkeStructure, World

# Definir una estructura temporal de Kripke
k = KripkeStructure()
k['a'] = {0: [1]}
k['b'] = {0: [2]}
k['c'] = {1: [2]}

# Consultas
print("¿a es válido en el mundo 0?", k.satisfies('a', 0))  # True
print("¿b es válido en el mundo 0?", k.satisfies('b', 0))  # False
print("¿c es válido en el mundo 1?", k.satisfies('c', 1))  # True

# Fórmula temporal
formula = parse('G((F a) -> (F b))')

# Modelo de Kripke
k = KripkeStructure()
k['a'] = {0: [1], 1: [2]}
k['b'] = {0: [2], 1: [2]}

# Consultar la fórmula temporal en el modelo de Kripke
print("¿G((F a) -> (F b)) es válido en el modelo de Kripke?", k.satisfies(formula))  # True
