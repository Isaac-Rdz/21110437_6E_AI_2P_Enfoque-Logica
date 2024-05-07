
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def is_applicable(self, state):
        return all(condition in state for condition in self.preconditions)

    def apply(self, state):
        if self.is_applicable(state):
            new_state = state.copy()
            for effect in self.effects:
                new_state.add(effect)
            return new_state
        else:
            return None

class STRIPSPlanner:
    def __init__(self, actions, initial_state, goal_state):
        self.actions = actions
        self.initial_state = initial_state
        self.goal_state = goal_state

    def plan(self):
        current_state = self.initial_state
        plan = []

        while current_state != self.goal_state:
            applicable_actions = [action for action in self.actions if action.is_applicable(current_state)]
            if not applicable_actions:
                return None  # No se encontró un plan

            next_action = applicable_actions[0]  # Seleccionar la primera acción aplicable
            current_state = next_action.apply(current_state)
            plan.append(next_action)
        
        return plan

# Definir acciones y estados iniciales y objetivos
actions = [
    Action("agarrar_pan", {"pan_disponible"}, {"pan_en_la_mano"}),
    Action("agarrar_jamon", {"jamon_disponible"}, {"jamon_en_la_mano"}),
    Action("hacer_sandwich", {"pan_en_la_mano", "jamon_en_la_mano"}, {"sandwich_hecho"}),
]

initial_state = {"pan_disponible", "jamon_disponible"}
goal_state = {"sandwich_hecho"}

# Crear un planificador STRIPS
planner = STRIPSPlanner(actions, initial_state, goal_state)

# Planificar y mostrar el plan
plan = planner.plan()
if plan:
    print("Plan encontrado:")
    for action in plan:
        print(action.name)
else:
    print("No se encontró un plan.")
