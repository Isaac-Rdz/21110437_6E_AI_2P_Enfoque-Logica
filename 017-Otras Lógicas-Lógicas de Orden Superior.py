
 from pyswip import Prolog

# Crear un objeto Prolog
prolog = Prolog()

# Definir hechos y reglas con lógica de orden superior
prolog.assertz("es_par(X) :- X mod 2 =:= 0")
prolog.assertz("es_impar(X) :- X mod 2 =:= 1")
prolog.assertz("aplicar(Func, X, Resultado) :- call(Func, X, Resultado)")

# Consultar
for solucion in prolog.query("aplicar(es_par, 4, R)"):
    print("Resultado:", solucion["R"])

for solucion in prolog.query("aplicar(es_impar, 5, R)"):
    print("Resultado:", solucion["R"])
