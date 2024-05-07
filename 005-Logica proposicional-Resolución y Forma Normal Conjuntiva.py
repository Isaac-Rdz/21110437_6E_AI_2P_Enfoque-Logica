
from sympy import symbols, satisfiable, to_cnf

# Definir símbolos
p, q, r = symbols('p q r')

# Definir proposiciones
proposicion1 = (p | ~q) & (q | r)
proposicion2 = ~(p & q) | (q & r)

# Verificar si las proposiciones son satisfacibles
print("¿La proposición 1 es satisfacible?", satisfiable(proposicion1))
print("¿La proposición 2 es satisfacible?", satisfiable(proposicion2))

# Convertir proposiciones a Forma Normal Conjuntiva (FNC)
fnc1 = to_cnf(proposicion1)
fnc2 = to_cnf(proposicion2)

print("FNC de la proposición 1:", fnc1)
print("FNC de la proposición 2:", fnc2)
