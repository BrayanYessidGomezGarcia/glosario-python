import mensajeError
import listasCampus

def horarioAgregado():
    print("AGREGAR HORARIO")

    nom_jornada= input("Ingresa el nombre de la Jornada: ")
    while not nom_jornada:
       mensajeError.msgError("La Jornada no puede estar Vacia")
       nom_jornada= input("Ingresa el nombre de la Jornada: ")

    codigo= None
    while codigo is None:
        try:
            codigo= int(input("Ingrese el codigo: "))
        except ValueError:
            mensajeError.msgError("Codigo invalido")

    hora_inicio= input("Ingrese hora de Inicio: ")
    while not hora_inicio:
       mensajeError.msgError("La hora de inicio no puede estar Vacia")
       hora_inicio= input("Ingresa hora de Inicio: ")

    hora_fin= input("Ingrese hora de fin: ")
    while not hora_fin:
       mensajeError.msgError("La hora de fin no puede estar Vacia")
       hora_fin= input("Ingresa la hora de fin: ")

    diccionario_horario= {
        "NombreJornada": nom_jornada,
        "Codigo": codigo,
        "Hora": {
            "HoraInicio": hora_inicio,
            "HoraFinal": hora_fin
        }
    }

    listaHorario = listasCampus.cargarHorarios()
    listaHorario.append(diccionario_horario)
    listasCampus.guardarHorarios(listaHorario)
