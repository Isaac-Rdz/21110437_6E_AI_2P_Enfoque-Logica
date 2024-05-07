
 class SistemaRecomendacion:
    def __init__(self):
        self.base_conocimiento = {
            "Usuario1": {"Titanic", "The Shawshank Redemption", "Inception"},
            "Usuario2": {"The Shawshank Redemption", "Forrest Gump", "The Godfather"},
            "Usuario3": {"Inception", "The Godfather", "Pulp Fiction"},
            "Usuario4": {"The Shawshank Redemption", "Forrest Gump", "The Godfather"}
        }

    def recomendar_peliculas(self, usuario):
        peliculas_vistas = self.base_conocimiento[usuario]
        peliculas_recomendadas = set()

        for otro_usuario, peliculas in self.base_conocimiento.items():
            if otro_usuario != usuario:
                peliculas_recomendadas.update(peliculas - peliculas_vistas)

        return peliculas_recomendadas

# Ejemplo de uso
sistema = SistemaRecomendacion()

usuario = "Usuario1"
peliculas_recomendadas = sistema.recomendar_peliculas(usuario)

print("Peliculas recomendadas para", usuario, ":", peliculas_recomendadas)
