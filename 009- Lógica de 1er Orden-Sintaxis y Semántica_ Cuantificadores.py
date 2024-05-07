
 from sympy import symbols, forall, exists

# Definir símbolos
x, y = symbols('x y')

# Cuantificador universal (para todo)
enunciado_universal = forall(x, x**2 >= 0)

# Cuantificador existencial (existe al menos uno)
enunciado_existencial = exists(y, y + 1 == 0)

# Imprimir enunciados
print("Cuantificador universal (para todo x, x^2 >= 0):", enunciado_universal)
print("Cuantificador existencial (existe y, y + 1 == 0):", enunciado_existencial)
