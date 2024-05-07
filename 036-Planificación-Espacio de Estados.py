
from collections import deque

# Definición de un grafo como un diccionario de listas de adyacencia
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 3, 'E': 2},
    'C': {'F': 4},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Función para realizar una búsqueda en anchura en el espacio de estados
def bfs_search(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # Tupla de (nodo, camino)
    
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(current)
        for neighbor, _ in graph.get(current, {}).items():
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Ejemplo de uso de la búsqueda en anchura en el espacio de estados
start_state = 'A'
goal_state = 'F'
shortest_path = bfs_search(graph, start_state, goal_state)

# Imprimir el camino más corto encontrado
if shortest_path:
    print("El camino más corto desde {} hasta {} es:".format(start_state, goal_state))
    print(" -> ".join(shortest_path))
else:
    print("No se encontró un camino desde {} hasta {}.".format(start_state, goal_state))
