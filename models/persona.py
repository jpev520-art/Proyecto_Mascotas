class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


class Adoptante(Persona):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.mascotas_adoptadas = []

    def adoptar(self, mascota):
        self.mascotas_adoptadas.append(mascota)