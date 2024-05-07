
class SistemaInferencia:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def encadenamiento_hacia_adelante(self, hechos_iniciales):
        hechos = set(hechos_iniciales)
        nuevos_hechos = True

        while nuevos_hechos:
            nuevos_hechos = False
            for regla in self.base_conocimiento:
                antecedentes, consecuente = regla[:-1], regla[-1]
                if all(hecho in hechos for hecho in antecedentes) and consecuente not in hechos:
                    hechos.add(consecuente)
                    nuevos_hechos = True

        return hechos

    def encadenamiento_hacia_atras(self, meta, hechos_iniciales):
        if meta in hechos_iniciales:
            return True
        for regla in self.base_conocimiento:
            antecedentes, consecuente = regla[:-1], regla[-1]
            if consecuente == meta and all(self.encadenamiento_hacia_atras(antecedente, hechos_iniciales) for antecedente in antecedentes):
                return True
        return False

# Ejemplo de uso
base_conocimiento = {
    ('P', 'Q'): 'R',
    ('R',): 'S',
    ('S',): 'T'
}
sistema = SistemaInferencia(base_conocimiento)

# Encadenamiento hacia adelante
hechos_iniciales = {'P', 'Q'}
hechos = sistema.encadenamiento_hacia_adelante(hechos_iniciales)
print("Hechos deducidos hacia adelante:", hechos)

# Encadenamiento hacia atrás
meta = 'T'
resultado = sistema.encadenamiento_hacia_atras(meta, hechos_iniciales)
print("¿Se puede deducir la meta 'T'?", resultado)
