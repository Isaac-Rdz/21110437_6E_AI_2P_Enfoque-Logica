
class MotorInferencia:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def resolver(self, pregunta):
        clausula_negada = self.negar_pregunta(pregunta)
        clausula_completa = self.base_conocimiento + clausula_negada

        while True:
            nueva_clausula = self.generar_nuevas_clausulas(clausula_completa)
            if not nueva_clausula:
                return False  # No se puede inferir la pregunta
            if set(nueva_clausula).issubset(clausula_completa):
                return True   # La pregunta es verdadera
            clausula_completa += nueva_clausula

    def negar_pregunta(self, pregunta):
        return ['~' + predicado for predicado in pregunta]

    def generar_nuevas_clausulas(self, clausulas):
        nuevas_clausulas = []
        for i, clausula1 in enumerate(clausulas):
            for j, clausula2 in enumerate(clausulas):
                if i != j:
                    resolvente = self.resolver_clausulas(clausula1, clausula2)
                    if resolvente and resolvente not in clausulas and resolvente not in nuevas_clausulas:
                        nuevas_clausulas.append(resolvente)
        return nuevas_clausulas

    def resolver_clausulas(self, clausula1, clausula2):
        for predicado in clausula1:
            if predicado.startswith('~'):
                complemento = predicado[1:]
            else:
                complemento = '~' + predicado
            if complemento in clausula2:
                clausula_resultante = clausula1.copy()
                clausula_resultante.remove(predicado)
                clausula_resultante.remove(complemento)
                if not clausula_resultante:
                    return ['Resuelto']  # Clausulas cancelan mutuamente
                else:
                    return clausula_resultante
        return None


# Ejemplo de uso
base_conocimiento = [['P'], ['~P', 'Q'], ['~Q', 'R']]
motor = MotorInferencia(base_conocimiento)

# Consulta
pregunta = ['R']
resultado = motor.resolver(pregunta)

# Imprimir resultado
if resultado:
    print("La pregunta es verdadera.")
else:
    print("La pregunta es falsa.")
