
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables de entrada y salida
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de membresía para las variables de entrada y salida
calidad.automf(3)
servicio.automf(3)
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Definir reglas difusas
regla1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
regla2 = ctrl.Rule(service['average'], tip['medium'])
regla3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# Crear sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Entradas al sistema
sistema.input['calidad'] = 6.5
sistema.input['servicio'] = 9.8

# Computar la salida
sistema.compute()

# Mostrar la salida
print("Propina calculada:", sistema.output['propina'])
