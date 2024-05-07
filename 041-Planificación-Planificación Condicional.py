
class ConditionalPlanning:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def plan(self):
        current_state = self.initial_state.copy()
        plan = []

        while current_state != self.goal_state:
            next_action = None
            for action in self.actions:
                if action.condition(current_state):
                    next_action = action
                    break

            if next_action is None:
                print("No se pudo encontrar una acción para alcanzar el objetivo.")
                return None

            plan.append(next_action)
            current_state = next_action.result(current_state)

        return plan

class Action:
    def __init__(self, name, condition, effect):
        self.name = name
        self.condition = condition
        self.effect = effect

    def result(self, state):
        return state.union(self.effect)

# Ejemplo de uso
initial_state = {"A"}
goal_state = {"D"}

# Definir acciones
actions = [
    Action("Action 1", lambda state: "A" in state, {"B"}),
    Action("Action 2", lambda state: "B" in state, {"C"}),
    Action("Action 3", lambda state: "C" in state, {"D"})
]

planner = ConditionalPlanning(initial_state, goal_state)
for action in actions:
    planner.add_action(action)

plan = planner.plan()
if plan:
    print("Plan:")
    for action in plan:
        print(action.name)
