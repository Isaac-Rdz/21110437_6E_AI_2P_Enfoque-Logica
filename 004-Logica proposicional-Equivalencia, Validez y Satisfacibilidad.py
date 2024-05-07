
from sympy import symbols, And, Or, Not, Implies, Equivalent, satisfiable, simplify_logic

# Definir símbolos
p, q, r = symbols('p q r')

# Definir proposiciones
proposicion1 = Equivalent(p, Or(Not(q), r))
proposicion2 = Or(Not(p), And(q, Not(r)))
proposicion3 = Implies(p, q)

# Verificar equivalencia
if proposicion1.equivalent(proposicion2):
    print("Las proposiciones 1 y 2 son equivalentes.")
else:
    print("Las proposiciones 1 y 2 no son equivalentes.")

# Verificar validez
if proposicion3.is_valid():
    print("La proposición 3 es válida.")
else:
    print("La proposición 3 no es válida.")

# Verificar satisfacibilidad
satisfacible = satisfiable(p & q & r)
if satisfacible:
    print("Las variables pueden satisfacerse para que la proposición sea verdadera.")
else:
    print("No hay asignación de variables que satisfaga la proposición.")
