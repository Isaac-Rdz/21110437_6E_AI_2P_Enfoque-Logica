
from pyDatalog import pyDatalog

# Definir hechos y reglas
pyDatalog.create_terms('padre, abuelo, X, Y, Z')

+padre("Juan", "Pedro")
+padre("Pedro", "Carlos")
+padre("Carlos", "Juan")

abuelo(X, Z) <= padre(X, Y) & padre(Y, Z)

# Consultar
print("Abuelos:")
print(abuelo(X, Y))
