
class ExecutionMonitor:
    def __init__(self, initial_plan):
        self.plan = initial_plan

    def monitor_execution(self):
        current_state = self.get_current_state()
        while not self.is_goal_reached(current_state):
            next_action = self.plan[0]
            print("Ejecutando:", next_action)
            # Simulación de ejecución de la acción
            self.plan = self.plan[1:]  # Eliminar la acción ejecutada
            current_state = self.get_current_state()

            # Aquí puedes agregar lógica para detectar cambios en el estado o eventos inesperados

            if self.is_replanning_needed(current_state):
                print("Replanificación necesaria.")
                self.replan()

    def get_current_state(self):
        # Simulación de obtener el estado actual del sistema
        return set(["A", "B"])  # Por ejemplo, un conjunto de eventos observados

    def is_goal_reached(self, current_state):
        # Simulación de verificar si se ha alcanzado el estado objetivo
        return "C" in current_state

    def is_replanning_needed(self, current_state):
        # Simulación de lógica para determinar si se necesita replanificación
        return "B" not in current_state

    def replan(self):
        # Simulación de generar un nuevo plan
        self.plan = ["Action 2", "Action 3"]

# Ejemplo de uso
initial_plan = ["Action 1", "Action 2", "Action 3"]
monitor = ExecutionMonitor(initial_plan)
monitor.monitor_execution()
