
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables de entrada y salida
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
potencia = ctrl.Consequent(np.arange(0, 101, 1), 'potencia')

# Definir funciones de membresía para las variables de entrada y salida
temperatura['fría'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['templada'] = fuzz.trimf(temperatura.universe, [0, 50, 100])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

humedad['seca'] = fuzz.trimf(humedad.universe, [0, 0, 50])
humedad['normal'] = fuzz.trimf(humedad.universe, [0, 50, 100])
humedad['húmeda'] = fuzz.trimf(humedad.universe, [50, 100, 100])

potencia['baja'] = fuzz.trimf(potencia.universe, [0, 0, 50])
potencia['media'] = fuzz.trimf(potencia.universe, [0, 50, 100])
potencia['alta'] = fuzz.trimf(potencia.universe, [50, 100, 100])

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['fría'] | humedad['seca'], potencia['alta'])
regla2 = ctrl.Rule(temperatura['templada'] & humedad['normal'], potencia['media'])
regla3 = ctrl.Rule(temperatura['caliente'] | humedad['húmeda'], potencia['baja'])

# Crear sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Entradas al sistema
sistema.input['temperatura'] = 80
sistema.input['humedad'] = 20

# Computar la salida
sistema.compute()

# Mostrar la salida
print("Potencia:", sistema.output['potencia'])
