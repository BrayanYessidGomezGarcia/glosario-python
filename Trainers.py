import mensajeError
import listasCampus
import os

def menuTrainer():
    while True:
        try:
            print("\n\n***CRUD DE TRAINERS***")
            print("\tMENU")
            print("1. Agregar Trainer")
            print("2. Modificar Trainer")
            print("3. Buscar Trainer")
            print("4. Salir")
            op = int(input("\t>>Escoja una opcion (1-4): "))
            if op < 1 or op > 5:
                mensajeError.msgError("Error. Opcion Invalida (de 1 a 4)")
                continue
            if op == 1:
                os.system("cls")
                trainerAgregado()
                input("Presione enter para volver al menu ")
            elif op == 2:
                os.system("cls")
                editarTrainer()
                input("Presione enter para volver al menu ")    
            elif op == 3:
                os.system("cls") 
                buscarTrainer()
                input("Presione enter para volver al menu ")     
            elif op == 4:
                os.system("cls")
                break  
            return op     
        except ValueError:
            mensajeError.msgError("Error. Opcion Invalida (de 1 a 5)")
            continue

#Funcion para agregar Trainers
def trainerAgregado():
    print("Formulario Trainer")

    id_trainer= None
    while id_trainer is None:
        try:
            id_trainer= int(input("Ingrese la identificacion del trainer: "))
        except ValueError:
            mensajeError.msgError("Identificacion invalida")
            
    nombre_trainer= input("Ingrese el nombre del Trainer: ")
    while not nombre_trainer:
        mensajeError.msgError("Nombre de Trainer Invalido")
        nombre_trainer= input("Ingrese el nombre del Trainer: ")

    esp_trainer= input("Ingrese la especializacion del trainer: ")
    while not esp_trainer:
        mensajeError.msgError("Especializacion no definida")
        esp_trainer= input("Ingrese la especializacion del trainer: ")


    edad_trainer= input("Ingrese la Edad: ")
    while not edad_trainer:
        mensajeError.msgError("Edad Invalida")
        edad_trainer= input("Ingrese la edad del Trainer: ")

    genero_trainer= input("Ingrese el Genero: ")
    while not genero_trainer:
        mensajeError.msgError("Genero Invalido")
        genero_trainer= input("Ingrese el Genero: ")

    diccionario_trainers= {
        "IdTrainer": id_trainer,
        "NombreTrainer": nombre_trainer,
        "Especializacion": esp_trainer,
        "Edad": edad_trainer,
        "Genero": genero_trainer
    }

    listaTrainer= listasCampus.cargarTrainers()
    listaTrainer.append(diccionario_trainers)
    listasCampus.guardarTrainers(listaTrainer)   
    print("Trainer Agregado Exitosamente")


#Funcion para listarTrainers
def listarTrainer():
    trainers = listasCampus.cargarTrainers()
    print("Lista de Trainers: ")
    for index, trainer in enumerate(trainers, start=1):
        print(f"{index}. {trainer['NombreTrainer']}")

#Funcion para modificar Trainers
def editarTrainer():
    print("MODIFICAR TRAINERS")
    listarTrainer()
    modificar_trainer = input("Ingrese el nombre del trainer que desea modificar: ")
    listTrainer = listasCampus.cargarTrainers()
    encontrado = False
    for trainer in listTrainer:
        if trainer['NombreTrainer'] == modificar_trainer:
            print("Trainer Encontrado: ")
            print(f"Identificacion: {trainer['IdTrainer']}")
            print(f"Nombre: {trainer['NombreTrainer']}")
            print(f"Especializacion: {trainer['Especializacion']}")
            print(f"Edad: {trainer['Edad']}")
            print(f"Genero: {trainer['Genero']}")
            print()
            
            pregunta = input("Desea Modificar la identificacion? (S/N)")                       
            if pregunta.upper() == "S":
                idTrainer = None
                while idTrainer is None:
                    try:
                        idTrainer = int(input("Nueva Identificacion: "))
                    except ValueError:
                        mensajeError.msgError("Numero no valido")
                trainer['IdTrainer'] = idTrainer
                    
            pregunta = input("Desea Modificar el nombre? (S/N)")                       
            if pregunta.upper() == "S":            
                trainer['NombreTrainer'] = input("Nuevo Nombre: ")
                while not trainer['NombreTrainer']:
                    mensajeError.msgError("El nombre no puede estar vacio")
                    trainer['NombreTrainer'] = input("Nuevo Nombre: ")
                
            pregunta = input("Desea Modificar la especializacion? (S/N)")                       
            if pregunta.upper() == "S":                
                trainer['Especializacion'] = input("Nueva especializacion: ")
                while not trainer['Especializacion']:
                    mensajeError.msgError("La especializacion no puede estar vacia")
                    trainer['Especializacion'] = input("Nueva Especializacion: ")    

            pregunta = input("Desea Modificar la edad? (S/N)")                       
            if pregunta.upper() == "S":
                trainer['Edad'] = input("Nueva Edad: ")
                while not trainer['Edad']:
                    mensajeError.msgError("La edad no puede estar vacia")
                    trainer['Edad'] = input("Nueva Edad: ")
                
            pregunta = input("Desea Modificar el genero? (S/N)")                       
            if pregunta.upper() == "S":                
                trainer['Genero'] = input("Nuevo Genero: ")
                while not trainer['Genero']:
                    mensajeError.msgError("El genero no puede estar vacio")
                    trainer['Genero'] = input("Nuevo Genero: ")
                     
            encontrado = True
            break       
    if encontrado:
        listasCampus.guardarTrainers(listTrainer)
        print("Trainer modificado exitosamente")
    else:
        print("Trainer no encontrado")                                    
            
#Funcion para buscar Trainers
def buscarTrainer():
    print("BUSCAR TRAINER")
    trainers = listasCampus.cargarTrainers()
    nombre_buscar = input("Ingrese el nombre del camper que desea buscar: ")
    encontrado = False
    for trainer in trainers:
        if trainer['NombreTrainer'] == nombre_buscar:
            encontrado = True
            print("Trainer encontrado:")
            print(f"Identificacion: {trainer['IdTrainer']}")
            print(f"Nombre: {trainer['NombreTrainer']}")
            print(f"Especialidad: {trainer['Especializacion']}")
            print(f"Edad: {trainer['Edad']}")
            print(f"Genero: {trainer['Genero']}")
            print()
    if not encontrado:
        print("Trainer no encontrado.")       
                



