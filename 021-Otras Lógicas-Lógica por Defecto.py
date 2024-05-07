
from clorm import Predicate, ComplexPredicate
from clorm import datalog

# Definir predicados
class Padre(Predicate):
    hijo = Predicate.Field()
    padre = Predicate.Field()

# Definir hechos
p1 = Padre("Juan", "Pedro")
p2 = Padre("Pedro", "Carlos")

# Definir reglas
reglas = datalog.DatalogProgram()
reglas += Padre("Juan", "Carlos")

# Consultar
for p in reglas.query(Padre("Juan", "X")):
    print(p.hijo, "es hijo de Juan")

for p in reglas.query(Padre("X", "Carlos")):
    print(p.hijo, "es hijo de Carlos")
