
class BaseConocimiento:
    def __init__(self):
        self.conocimiento = {}

    def agregar_conocimiento(self, concepto, informacion):
        self.conocimiento[concepto] = informacion

    def consultar_conocimiento(self, concepto):
        if concepto in self.conocimiento:
            return self.conocimiento[concepto]
        else:
            return "Lo siento, no tengo información sobre ese concepto."

# Crear una instancia de la base de conocimiento
base = BaseConocimiento()

# Agregar información a la base de conocimiento
base.agregar_conocimiento("Python", "Python es un lenguaje de programación interpretado de alto nivel.")

# Consultar información en la base de conocimiento
print(base.consultar_conocimiento("Python"))  # Imprime: Python es un lenguaje de programación interpretado de alto nivel.
print(base.consultar_conocimiento("IA"))      # Imprime: Lo siento, no tengo información sobre ese concepto.
