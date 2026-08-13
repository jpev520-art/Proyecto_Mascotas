from models.mascota import Mascota
from models.persona import Adoptante
from models.refugio import Refugio


def main():

    # Crear refugio
    refugio = Refugio()

    # Registrar mascotas
    mascota1 = Mascota("Max", "Perro", 3)
    mascota2 = Mascota("Luna", "Gato", 2)
    mascota3 = Mascota("Rocky", "Perro", 5)

    refugio.registrar_mascota(mascota1)
    refugio.registrar_mascota(mascota2)
    refugio.registrar_mascota(mascota3)

    # Crear adoptante
    adoptante = Adoptante("Juan", 28)

    # Menú
    while True:

        print("\n==============================")
        print("   SISTEMA DE ADOPCIÓN")
        print("==============================")
        print("1. Listar mascotas disponibles")
        print("2. Adoptar una mascota")
        print("3. Ver mascotas adoptadas")
        print("4. Salir")
        print("==============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            disponibles = refugio.listar_disponibles()

            print("\n--- MASCOTAS DISPONIBLES ---")

            if len(disponibles) == 0:
                print("No hay mascotas disponibles.")

            else:
                for mascota in disponibles:
                    print(mascota)

        elif opcion == "2":

            nombre = input("Ingrese el nombre de la mascota: ")

            refugio.asignar_adopcion(
                nombre,
                adoptante
            )

        elif opcion == "3":

            print("\n--- MASCOTAS ADOPTADAS ---")

            if len(adoptante.mascotas_adoptadas) == 0:
                print("Todavía no has adoptado ninguna mascota.")

            else:
                for mascota in adoptante.mascotas_adoptadas:
                    print(mascota)

        elif opcion == "4":

            print("Gracias por utilizar el sistema.")
            break

        else:

            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()