lista_super_heroes = ["Spider-Man", "Superman", "Batman"]

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n=== Gestión de Superhéroes ===")
    print("1. Listar superhéroes")
    print("2. Agregar superhéroe")
    print("3. Eliminar superhéroe")
    print("4. Salir")
    print("============================")

def listar_heroes():
    """Muestra la lista de superhéroes numerada."""
    if not lista_super_heroes:
        print("\nNo hay superhéroes en la lista.")
        return
    
    print("\nLista de Superhéroes:")
    for i, heroe in enumerate(lista_super_heroes, 1):
        print(f"{i}. {heroe}")

def agregar_heroe():
    """Agrega un nuevo superhéroe a la lista."""
    nuevo_heroe = input("\nIngresa el nombre del superhéroe: ").strip()
    if nuevo_heroe:
        if nuevo_heroe in lista_super_heroes:
            print(f"\n¡{nuevo_heroe} ya existe en la lista!")
        else:
            lista_super_heroes.append(nuevo_heroe)
            print(f"\n¡{nuevo_heroe} ha sido agregado exitosamente!")
    else:
        print("\nError: El nombre no puede estar vacío.")

def eliminar_heroe():
    """Elimina un superhéroe de la lista."""
    if not lista_super_heroes:
        print("\nNo hay superhéroes para eliminar.")
        return

    listar_heroes()
    heroe_eliminar = input("\nIngresa el nombre del superhéroe a eliminar: ").strip()
    
    try:
        lista_super_heroes.remove(heroe_eliminar)
        print(f"\n¡{heroe_eliminar} ha sido eliminado exitosamente!")
    except ValueError:
        print(f"\nError: {heroe_eliminar} no se encuentra en la lista.")

def salir():
    """Termina la ejecución del programa."""
    print("\n¡Gracias por usar el programa! ¡Hasta pronto!")
    exit()

def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-4): ").strip()
        
        opciones = {
            "1": listar_heroes,
            "2": agregar_heroe,
            "3": eliminar_heroe,
            "4": salir
        }
        
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("\nError: Opción inválida. Por favor, elige una opción entre 1 y 4.")

if __name__ == "__main__":
    main()