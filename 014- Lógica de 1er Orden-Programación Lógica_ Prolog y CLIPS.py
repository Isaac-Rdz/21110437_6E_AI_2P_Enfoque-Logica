
 from pyswip import Prolog
import clips

# Uso de Prolog
prolog = Prolog()
prolog.assertz("padre(juan, maria)")
prolog.assertz("padre(pedro, juan)")

# Uso de CLIPS
env = clips.Environment()
env.load("reglas.clp")
env.run()

# Obtener resultados de Prolog
for solucion in prolog.query("padre(X, Y)"):
    print("Prolog:", solucion["X"], "es padre de", solucion["Y"])

# Obtener resultados de CLIPS
for fact in env.facts():
    if fact.template.name == "padre":
        print("CLIPS:", fact[1], "es padre de", fact[2])
x
