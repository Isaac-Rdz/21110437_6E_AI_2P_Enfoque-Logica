
class MotorInferencia:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def encadenamiento_hacia_adelante(self, hechos):
        nuevos_hechos = hechos.copy()
        cambios = True

        while cambios:
            cambios = False
            for regla in self.base_conocimiento:
                antecedentes, consecuente = regla[:-1], regla[-1]
                if all(antecedente in hechos for antecedente in antecedentes) and consecuente not in hechos:
                    nuevos_hechos.add(consecuente)
                    cambios = True

        return nuevos_hechos

    def encadenamiento_hacia_atras(self, meta, hechos):
        if meta in hechos:
            return True
        else:
            for regla in self.base_conocimiento:
                antecedentes, consecuente = regla[:-1], regla[-1]
                if consecuente == meta:
                    if all(self.encadenamiento_hacia_atras(antecedente, hechos) for antecedente in antecedentes):
                        return True
            return False

# Ejemplo de uso
base_conocimiento = {('P', 'Q'), ('Q', 'R'), ('R', 'S')}
motor = MotorInferencia(base_conocimiento)

# Encadenamiento hacia adelante
hechos_iniciales = {'P'}
nuevos_hechos = motor.encadenamiento_hacia_adelante(hechos_iniciales)
print("Hechos tras encadenamiento hacia adelante:", nuevos_hechos)

# Encadenamiento hacia atrás
meta = 'S'
resultado = motor.encadenamiento_hacia_atras(meta, hechos_iniciales)
print("¿Se puede demostrar la meta 'S'?", resultado)
