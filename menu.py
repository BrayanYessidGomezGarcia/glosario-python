import mensajeError

def menuCampus():

    while True:
        try:
            print("\n\n***SISTEMA DE CAMPUS***")
            print("\tMENU")
            print("1. CRUD CAMPER")
            print("2. Asignar Notas")
            print("3. Agregar Rutas")
            print("4. Agregar Horario")
            print("5. Formulario Trainer")
            op = int(input("\t>>Escoja una opcion (1-5): "))
            if op < 1 or op > 5:
                mensajeError.msgError("Error. Opcion Invalida (de 1 a 5)")
                continue
            return op
        
        except ValueError:
            mensajeError.msgError("Error. Opcion Invalida (de 1 a 5)")
            continue
            
          


