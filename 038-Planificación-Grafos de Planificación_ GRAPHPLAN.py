
import networkx as nx

class GraphPlan:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions
        self.graph = nx.DiGraph()
        self.layers = []

    def add_layer(self, layer):
        self.layers.append(layer)

    def apply_actions(self):
        for action in self.actions:
            for preconditions, effects in action:
                for layer in reversed(self.layers):
                    if all(state in layer for state in preconditions):
                        new_layer = layer.union(effects)
                        if new_layer not in self.layers:
                            self.add_layer(new_layer)
                            self.graph.add_edge(layer, new_layer, action=str(action))
                            break

    def is_goal_reached(self):
        return self.goal_state in self.layers[-1]

    def extract_plan(self):
        if not self.is_goal_reached():
            return None
        plan = []
        current_layer = self.layers[-1]
        while current_layer != self.initial_state:
            predecessors = list(self.graph.predecessors(current_layer))
            edge_data = self.graph.get_edge_data(predecessors[0], current_layer)
            plan.append(edge_data['action'])
            current_layer = predecessors[0]
        return plan[::-1]

    def find_plan(self):
        self.add_layer(self.initial_state)
        while not self.is_goal_reached():
            self.apply_actions()
        return self.extract_plan()

# Ejemplo de uso
initial_state = {"A"}
goal_state = {"D"}
actions = [
    ([{"A"}], {"B"}),
    ([{"B"}], {"C"}),
    ([{"C"}], {"D"}),
    ([{"D"}], {"E"}),
    ([{"E"}], {"F"})
]

planner = GraphPlan(initial_state, goal_state, actions)
plan = planner.find_plan()
print("Plan:", plan)
