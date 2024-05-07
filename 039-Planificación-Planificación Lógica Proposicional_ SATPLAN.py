
import pycosat

class SATPlan:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def cnf_encoding(self):
        cnf = []

        # Codificación del estado inicial
        for state in self.initial_state:
            cnf.append([state])

        # Codificación del objetivo
        goal_clause = [state for state in self.goal_state]
        cnf.append(goal_clause)

        # Codificación de las acciones
        for action in self.actions:
            for precond in action[0]:
                for effect in action[1]:
                    cnf.append([-precond, effect])

        return cnf

    def find_plan(self):
        cnf = self.cnf_encoding()
        solution = pycosat.solve(cnf)

        if solution == "UNSAT":
            return None

        plan = []
        for variable in solution:
            if variable > 0 and variable in self.goal_state:
                plan.append(variable)
        return plan

# Ejemplo de uso
initial_state = {1}
goal_state = {4}
actions = [
    ([1], [2]),
    ([2], [3]),
    ([3], [4]),
    ([4], [5]),
    ([5], [6])
]

planner = SATPlan(initial_state, goal_state, actions)
plan = planner.find_plan()
print("Plan:", plan)
