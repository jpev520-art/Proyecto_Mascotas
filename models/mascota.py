class Mascota:

    def __init__(self, nombre, especie, edad, adoptado=False):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = adoptado

    def __str__(self):
        estado = "Adoptado" if self.adoptado else "Disponible"

        return (
            f"Nombre: {self.nombre} | "
            f"Especie: {self.especie} | "
            f"Edad: {self.edad} años | "
            f"Estado: {estado}"
        )
