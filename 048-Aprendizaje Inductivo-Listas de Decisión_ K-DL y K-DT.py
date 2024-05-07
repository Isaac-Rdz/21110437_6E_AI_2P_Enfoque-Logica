
class KDNode:
    def __init__(self, point, split_dim):
        self.point = point
        self.split_dim = split_dim
        self.left = None
        self.right = None

class KDTree:
    def __init__(self, points):
        self.root = self._build_kdtree(points)

    def _build_kdtree(self, points, depth=0):
        if len(points) == 0:
            return None

        k = len(points[0])
        split_dim = depth % k

        points.sort(key=lambda x: x[split_dim])
        median_index = len(points) // 2

        node = KDNode(points[median_index], split_dim)
        node.left = self._build_kdtree(points[:median_index], depth + 1)
        node.right = self._build_kdtree(points[median_index + 1:], depth + 1)

        return node

    def _distance(self, p1, p2):
        return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

    def _search_nearest_neighbor(self, query_point, node, depth=0, best=None):
        if node is None:
            return best

        k = len(query_point)
        split_dim = node.split_dim

        if best is None or self._distance(query_point, node.point) < self._distance(query_point, best):
            best = node.point

        if query_point[split_dim] < node.point[split_dim]:
            next_node = node.left
            other_node = node.right
        else:
            next_node = node.right
            other_node = node.left

        best = self._search_nearest_neighbor(query_point, next_node, depth + 1, best)

        if (query_point[split_dim] - node.point[split_dim]) ** 2 < self._distance(query_point, best):
            best = self._search_nearest_neighbor(query_point, other_node, depth + 1, best)

        return best

    def find_nearest_neighbor(self, query_point):
        return self._search_nearest_neighbor(query_point, self.root)

# Ejemplo de uso
points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
kdtree = KDTree(points)
query_point = (9, 2)
nearest_neighbor = kdtree.find_nearest_neighbor(query_point)
print("Nearest Neighbor:", nearest_neighbor)
