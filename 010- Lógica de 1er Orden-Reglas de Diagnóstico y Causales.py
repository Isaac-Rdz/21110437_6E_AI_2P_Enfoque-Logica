
 class SistemaDiagnostico:
    def __init__(self):
        self.base_conocimiento = {
            "Síntoma1": {"Causa1", "Causa2"},
            "Síntoma2": {"Causa2", "Causa3"},
            "Síntoma3": {"Causa1", "Causa3"}
        }

    def diagnosticar(self, sintomas):
        posibles_causas = set()

        for sintoma in sintomas:
            if sintoma in self.base_conocimiento:
                posibles_causas.update(self.base_conocimiento[sintoma])

        return posibles_causas

# Ejemplo de uso
sistema = SistemaDiagnostico()

sintomas = ["Síntoma1", "Síntoma3"]
causas_posibles = sistema.diagnosticar(sintomas)

print("Posibles causas:", causas_posibles)
