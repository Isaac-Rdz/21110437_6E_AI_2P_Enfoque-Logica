
class Categoria:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
        self.hijos = []

        if padre:
            padre.agregar_hijo(self)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

class Objeto:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

# Definir categorías
animal = Categoria("Animal")
mamifero = Categoria("Mamífero", animal)
reptil = Categoria("Reptil", animal)
perro = Categoria("Perro", mamifero)
gato = Categoria("Gato", mamifero)
iguana = Categoria("Iguana", reptil)
serpiente = Categoria("Serpiente", reptil)

# Definir objetos
oso = Objeto("Oso", mamifero)
leon = Objeto("León", mamifero)
labrador = Objeto("Labrador", perro)
siames = Objeto("Siamés", gato)
verde = Objeto("Verde", iguana)
piton = Objeto("Pitón", serpiente)

# Consultar la jerarquía de categorías
def imprimir_categorias(categoria, nivel=0):
    print("  " * nivel + categoria.nombre)
    for hijo in categoria.hijos:
        imprimir_categorias(hijo, nivel + 1)

print("Jerarquía de categorías:")
imprimir_categorias(animal)

# Consultar objetos en una categoría específica
def objetos_en_categoria(categoria):
    print(f"Objetos en la categoría '{categoria.nombre}':")
    for objeto in objetos:
        if objeto.categoria == categoria:
            print(objeto.nombre)

objetos = [oso, leon, labrador, siames, verde, piton]
objetos_en_categoria(perro)
