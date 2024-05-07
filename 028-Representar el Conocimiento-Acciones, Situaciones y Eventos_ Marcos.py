
class Marco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

    def agregar_atributo(self, nombre, valor):
        self.atributos[nombre] = valor

    def obtener_atributo(self, nombre):
        return self.atributos.get(nombre, None)

# Definir marcos para diferentes conceptos
persona = Marco("Persona")
animal = Marco("Animal")
objeto = Marco("Objeto")

# Agregar atributos a los marcos
persona.agregar_atributo("nombre", "Juan")
persona.agregar_atributo("edad", 30)
animal.agregar_atributo("especie", "León")
objeto.agregar_atributo("tipo", "Mesa")
objeto.agregar_atributo("color", "Marrón")

# Consultar atributos de los marcos
print("Nombre de la persona:", persona.obtener_atributo("nombre"))
print("Edad de la persona:", persona.obtener_atributo("edad"))
print("Especie del animal:", animal.obtener_atributo("especie"))
print("Tipo del objeto:", objeto.obtener_atributo("tipo"))
print("Color del objeto:", objeto.obtener_atributo("color"))
