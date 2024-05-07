
class ResolucionSkolem:
    def __init__(self):
        pass

    def negar_literal(self, literal):
        if literal.startswith("~"):
            return literal[1:]
        else:
            return "~" + literal

    def skolemizar(self, formula):
        # Simplificación de la fórmula: negar y convertir a cláusulas
        clausulas = [set(literal.split(" v ")) for literal in formula.split(" ^ ")]
        clausulas_negadas = [{self.negar_literal(literal)} for literal in formula.split(" ^ ")]

        # Agregar cláusulas negadas a las cláusulas originales
        clausulas.extend(clausulas_negadas)

        # Resolución
        while True:
            nuevas_clausulas = set()
            num_clausulas = len(clausulas)

            for i in range(num_clausulas):
                for j in range(i + 1, num_clausulas):
                    resolvente = self.resolver_clausulas(clausulas[i], clausulas[j])
                    if not resolvente:
                        continue
                    if not resolvente:  # Si resolvente es la cláusula vacía, la fórmula es insatisfacible
                        return False
                    nuevas_clausulas.add(resolvente)

            if nuevas_clausulas.issubset(clausulas):
                return True  # No se puede agregar más cláusulas
            clausulas.update(nuevas_clausulas)

    def resolver_clausulas(self, clausula1, clausula2):
        for literal in clausula1:
            if self.negar_literal(literal) in clausula2:
                resolvente = clausula1.union(clausula2) - {literal} - {self.negar_literal(literal)}
                if not resolvente:
                    return None
                return frozenset(resolvente)
        return None

# Ejemplo de uso
resolucion_skolem = ResolucionSkolem()

formula = "(P(x) ^ Q(x)) v ~P(f(y))"
resultado = resolucion_skolem.skolemizar(formula)

print("La fórmula es satisfacible:", resultado)
