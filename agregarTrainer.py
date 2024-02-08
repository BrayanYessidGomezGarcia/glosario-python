import mensajeError
import listasCampus

def trainerAgregado():
    print("Formulario Trainer")

    nombre_trainer= input("Ingrese el nombre del Trainer: ")
    while not nombre_trainer:
        mensajeError.msgError("Nombre de Trainer Invalido")
        nombre_trainer= input("Ingrese el nombre del Trainer: ")

    codigo_trainer= None
    while codigo_trainer is None:
        try:
            codigo_trainer= int(input("Ingrese el codigo: "))
        except ValueError:
            mensajeError.msgError("Codigo invalido")

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
        "NombreTrainer": nombre_trainer,
        "CodigoTrainer": codigo_trainer,
        "Especializacion": esp_trainer,
        "Edad": edad_trainer,
        "Genero": genero_trainer
    }

    listaTrainer= listasCampus.cargarTrainers()
    listaTrainer.append(diccionario_trainers)
    listasCampus.guardarTrainers(listaTrainer)




