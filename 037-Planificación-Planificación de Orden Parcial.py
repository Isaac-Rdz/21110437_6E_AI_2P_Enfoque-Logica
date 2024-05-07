
from collections import defaultdict

class PartialOrderPlanner:
    def __init__(self, actions, constraints):
        self.actions = actions
        self.constraints = constraints
    
    def plan(self):
        order = []
        unresolved = set(self.actions)
        before = defaultdict(set)
        after = defaultdict(set)
        
        # Construir grafos de precedencia
        for a, b in self.constraints:
            before[b].add(a)
            after[a].add(b)
        
        # Resolver restricciones transitivas
        while unresolved:
            action_with_no_before = unresolved.difference(before.keys())
            for action in action_with_no_before:
                unresolved.remove(action)
                order.append(action)
                for b in after[action]:
                    before[b].remove(action)
                    if not before[b]:
                        unresolved.add(b)
        
        return order

# Ejemplo de uso
actions = {'A', 'B', 'C', 'D', 'E'}
constraints = {('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E')}

planner = PartialOrderPlanner(actions, constraints)
order = planner.plan()

print("Planificación de Orden Parcial:")
print(order)
