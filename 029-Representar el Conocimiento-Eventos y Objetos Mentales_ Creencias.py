
class Agente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.creencias = {}

    def agregar_creencia(self, evento, creencia):
        if evento not in self.creencias:
            self.creencias[evento] = []
        self.creencias[evento].append(creencia)

    def obtener_creencias(self, evento):
        return self.creencias.get(evento, [])

# Definir un agente
agente = Agente("Juan")

# Agregar creencias sobre eventos y objetos mentales
agente.agregar_creencia("Situación 1", "Juan cree que el cielo está despejado")
agente.agregar_creencia("Situación 1", "Juan cree que es un buen día para salir a caminar")
agente.agregar_creencia("Situación 2", "Juan cree que va a llover")

# Consultar las creencias del agente sobre eventos
print("Creencias del agente sobre Situación 1:")
for creencia in agente.obtener_creencias("Situación 1"):
    print("-", creencia)

print("\nCreencias del agente sobre Situación 2:")
for creencia in agente.obtener_creencias("Situación 2"):
    print("-", creencia)
