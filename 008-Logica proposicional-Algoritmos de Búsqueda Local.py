
 import random
import math

def funcion_objetivo(x):
    return -x**2 + 5*x + 10  # Función cuadrática simple

def hill_climbing(funcion_objetivo, paso=0.1, intentos_maximos=1000):
    x = random.uniform(-10, 10)  # Inicialización aleatoria
    valor_actual = funcion_objetivo(x)

    for _ in range(intentos_maximos):
        paso_x = random.uniform(-paso, paso)
        nuevo_x = x + paso_x
        nuevo_valor = funcion_objetivo(nuevo_x)

        if nuevo_valor > valor_actual:
            x, valor_actual = nuevo_x, nuevo_valor

    return x, valor_actual

# Ejemplo de uso
x_maximo, valor_maximo = hill_climbing(funcion_objetivo)

print("Máximo local encontrado en x = {:.2f} con un valor de {:.2f}".format(x_maximo, valor_maximo))
