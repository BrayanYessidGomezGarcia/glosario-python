import mensajeError


def menuCampus():

    while True:
        try:
            print("\n\n***SISTEMA DE CAMPUS***")
            print("\tMENU")
            print("1. CRUD CAMPER")
            print("2. CRUD TRAINERS")
            print("3. Agregar Rutas")
            print("4. Asignaciones")
            print("5. Matricular")
            print("6. Evaluar Campers")
            print("7. Listar Campers en Riesgo")
            print("8. Reportes")
            print("9. Salir")
            op = int(input("\t>>Escoja una opcion (1-9): "))
            if op < 1 or op > 9:
                mensajeError.msgError("Error. Opcion Invalida (de 1 a 9)")
                continue
            return op

        except ValueError:
            mensajeError.msgError("Error. Opcion Invalida (de 1 a 9)")
            continue
