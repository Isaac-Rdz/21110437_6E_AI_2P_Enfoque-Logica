
class SistemaExperto:
    def __init__(self):
        self.base_conocimiento = {}

    def agregar_regla(self, condicion, conclusion):
        if condicion in self.base_conocimiento:
            self.base_conocimiento[condicion].append(conclusion)
        else:
            self.base_conocimiento[condicion] = [conclusion]

    def consultar(self, condicion):
        if condicion in self.base_conocimiento:
            return self.base_conocimiento[condicion]
        else:
            return ["No se encontraron conclusiones para esta condición."]

# Crear un sistema experto
sistema_experto = SistemaExperto()

# Agregar reglas al sistema experto
sistema_experto.agregar_regla("tiene_fiebre", "posible_enfermedad: gripe")
sistema_experto.agregar_regla("tiene_fiebre and dolor_garganta", "posible_enfermedad: faringitis")
sistema_experto.agregar_regla("tiene_fiebre and dolor_cabeza", "posible_enfermedad: migraña")

# Consultar el sistema experto con una condición
print("Posibles conclusiones para alguien que tiene fiebre:")
print(sistema_experto.consultar("tiene_fiebre"))
