
class NReinas:
    def __init__(self, N):
        self.N = N
        self.tablero = [[0] * N for _ in range(N)]

    def es_seguro(self, fila, columna):
        # Verifica si no hay reinas en la misma fila hacia la izquierda
        for i in range(columna):
            if self.tablero[fila][i]:
                return False

        # Verifica si no hay reinas en la diagonal superior izquierda
        for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
            if self.tablero[i][j]:
                return False

        # Verifica si no hay reinas en la diagonal inferior izquierda
        for i, j in zip(range(fila, self.N, 1), range(columna, -1, -1)):
            if self.tablero[i][j]:
                return False

        return True

    def resolver_n_reinas_util(self, columna):
        if columna >= self.N:
            return True

        for i in range(self.N):
            if self.es_seguro(i, columna):
                self.tablero[i][columna] = 1

                if self.resolver_n_reinas_util(columna + 1):
                    return True

                self.tablero[i][columna] = 0

        return False

    def resolver_n_reinas(self):
        if not self.resolver_n_reinas_util(0):
            print("No hay solución para {} reinas en un tablero de tamaño {}x{}.".format(self.N, self.N, self.N))
            return False

        self.imprimir_tablero()
        return True

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(' '.join(map(str, fila)))


# Ejemplo de uso
n = 8
n_reinas = NReinas(n)
n_reinas.resolver_n_reinas()
