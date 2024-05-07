
import networkx as nx
import matplotlib.pyplot as plt
from nltk.sem import Expression, Valuation, Model
from nltk.sem.logic import *

# Definir reglas
reglas = [
    ImpExpression(Variable("P"), Variable("Q")),
    AndExpression(ImpExpression(Variable("P"), Variable("Q")), ImpExpression(Variable("Q"), Variable("R"))),
    ImpExpression(Variable("S"), Variable("P")),
    OrExpression(ImpExpression(Variable("P"), Variable("R")), ImpExpression(Variable("S"), Variable("R")))
]

# Crear un modelo para evaluar las reglas
val = Valuation([('P', True), ('Q', True), ('R', False), ('S', False)])
modelo = Model(set(['P', 'Q', 'R', 'S']), val)

# Evaluar las reglas en el modelo
print("Evaluación de las reglas en el modelo:")
for regla in reglas:
    print(regla.simplify().simplify().evaluate(modelo))

# Crear un grafo para la red semántica
G = nx.DiGraph()

# Agregar nodos a la red semántica
G.add_node("Animal")
G.add_node("Perro")
G.add_node("Gato")

# Agregar arcos a la red semántica
G.add_edge("Animal", "Perro")
G.add_edge("Animal", "Gato")

# Visualizar la red semántica
plt.figure()
nx.draw(G, with_labels=True)
plt.show()

# Definir expresión en lógica descriptiva
expr = Expression.fromstring('all x.(man(x) -> mortal(x))')

# Imprimir la expresión
print("\nExpresión en lógica descriptiva:")
print(expr.simplify())
