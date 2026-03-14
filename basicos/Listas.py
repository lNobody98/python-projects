#Lista vacia
tareas = []

while True:
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    numero_tarea = int(input("Selecciona una opcion: "))
    if numero_tarea == 1:
        if len(tareas) == 0:
            print("No hay tareas")
        else:
            print("Tareas:")
            for i, tarea in enumerate(tareas):
                print(i + 1, tarea)
    elif numero_tarea == 2:
        tarea = input("Agregar tarea: ")
        tareas.append(tarea)
    elif numero_tarea == 3:
        if len(tareas) == 0:
            print("No hay tareas")
        else:
            numero_eliminar = int(input("Numero de tarea a eliminar: "))
            tareas.pop(numero_eliminar - 1)
    elif numero_tarea == 4:
        exit()
    else:
        print("Opcion no valida")
