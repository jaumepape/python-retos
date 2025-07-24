lista_super_heroes = ["Spider-Man", "Superman", "Batman"]

def mostrar_menu():
    print("Menú:")
    print("1. Listar")
    print("2. Agregar a la lista")
    print("3. Eliminar de la lista")
    print("4. Salir")


def Listar():
    for super_heroe in lista_super_heroes:
        print(super_heroe)

def Añadir():
    nuevo_super_heroe = input ("Ingresa un super héroe: ")
    lista_super_heroes.append(nuevo_super_heroe)

def Eliminar():
    eliminar_super_heroe = input ("Elimina un super héroe: ")
    lista_super_heroes.remove(eliminar_super_heroe)

def salir():
    print("Saliendo del programa")
    exit()


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            Listar()
        elif opcion == "2":
            Añadir()
        elif opcion == "3":
            Eliminar()
        elif opcion == "4":
            salir()
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()