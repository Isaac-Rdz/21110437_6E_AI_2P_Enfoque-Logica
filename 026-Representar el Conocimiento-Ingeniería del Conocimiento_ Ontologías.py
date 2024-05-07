
from owlready2 import *

# Crear una nueva ontología
onto = get_ontology("http://example.org/onto.owl")

# Definir clases y propiedades
with onto:
    class Persona(Thing):
        pass

    class Hombre(Persona):
        pass

    class Mujer(Persona):
        pass

    class tieneHijo(Property):
        domain = [Persona]
        range = [Persona]

# Guardar la ontología en un archivo
onto.save("mi_ontologia.owl")

# Cargar la ontología desde el archivo
onto = get_ontology("mi_ontologia.owl").load()

# Crear instancias
juan = Hombre("Juan")
maria = Mujer("Maria")

# Definir relaciones
juan.tieneHijo.append(maria)

# Consultas
print("Personas:")
for persona in onto.Persona.instances():
    print(persona)

print("\nHijos de Juan:")
for hijo in juan.tieneHijo:
    print(hijo)
