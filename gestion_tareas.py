tareas = []

def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
            
def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"La tarea '{tarea}' ha sido agregada")
    
def eliminar_tarea(indice):
    try:
        tareas.pop(indice - 1)
        print("La tarea ha sido eliminada")
    except IndexError:
        print("El índice de la tarea no existe")
        
def menu():
    print("\n Gestion de Tareas")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    
if __name__ == "__main__":
    while True:
        menu()
        
        option = input("Ingresa una opción 1, 2, 3 o 4 : ")
        if option == "1":
            mostrar_tareas()
        elif option == "2":
            tarea = input("Ingresa la nueva tarea: ")
            agregar_tarea(tarea)
        elif option == "3":
            indice = int(input("Ingresa el índice de la tarea a eliminar: "))
            eliminar_tarea(indice)
        elif option == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. ")