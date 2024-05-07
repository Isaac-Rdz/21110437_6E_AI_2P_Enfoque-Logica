
class Unificador:
    def __init__(self):
        pass

    def unificar(self, expresion1, expresion2):
        if expresion1 == expresion2:
            return {}

        if isinstance(expresion1, str) and expresion1[0].islower():
            return {expresion1: expresion2}

        if isinstance(expresion2, str) and expresion2[0].islower():
            return {expresion2: expresion1}

        if isinstance(expresion1, tuple) and isinstance(expresion2, tuple):
            head1, *tail1 = expresion1
            head2, *tail2 = expresion2
            unificacion_cabeza = self.unificar(head1, head2)
            if unificacion_cabeza is None:
                return None
            unificacion_cola = self.unificar(tail1, tail2)
            if unificacion_cola is None:
                return None
            unificacion_cabeza.update(unificacion_cola)
            return unificacion_cabeza

        return None

# Ejemplo de uso
unificador = Unificador()

expresion1 = ('padre', 'Juan', 'Maria')
expresion2 = ('padre', 'Juan', 'Ana')
resultado = unificador.unificar(expresion1, expresion2)

print("Unificación:", resultado)
