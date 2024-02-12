import listasCampus
import Campers
import mensajeError
import os
import json


def menuAsignacion():
    while True:
        try:
            print("\n\n***ASIGNACIONES***")
            print("\tMENU")
            print("1. Asignar Notas")
            print("2. Asignar Rutas")
            print("3. Salir")
            op = int(input("\t>>Escoja una opcion (1-3): "))
            if op < 1 or op > 3:
                mensajeError.msgError("Error. Opcion Invalida (de 1 a 3)")
                continue
            if op == 1:
                os.system("cls")
                NotasAsignadas()
                input("Presione enter para volver al menu ")
            elif op == 2:
                os.system("cls")
                menuAsignacionesRutas()
            elif op == 3:
                os.system("cls")
                break
            return op

        except ValueError:
            mensajeError.msgError("Error. Opcion Invalida (de 1 a 3)")
            continue


def menuAsignacionesRutas():
    while True:
        try:
            print("\n\n***ASIGNACIONES RUTAS***")
            print("\tMENU")
            print("1. Asignar Ruta a Camper")
            print("2. Asignar Ruta a Trainer")
            print("3. Salir")
            op = int(input("\t>>Escoja una opcion (1-3): "))
            if op < 1 or op > 3:
                mensajeError.msgError("Error. Opcion Invalida (de 1 a 3)")
                continue
            if op == 1:
                os.system("cls")
                asignarCamperaRuta()
                input("Presione enter para volver al menu ")
            elif op == 2:
                os.system("cls")
                asignarRutaTrainer()
                input("Presione enter para volver al menu ")
            elif op == 3:
                break
            return op
        except ValueError:
            mensajeError.msgError("Error. Opcion Invalida (de 1 a 3)")
            continue
        

def NotasAsignadas():
    mostrar_campers = listasCampus.cargarCampers()
    campers_inscritos = [
        camper for camper in mostrar_campers if camper["Estado"].lower() == "inscrito"
    ]
    if not mostrar_campers:
        print("No hay camper registrado. Por favor agregue uno")
        Campers.agregarCamper()
        return

    print("Lista de campers en estado de inscritos")
    for i, camper in enumerate(campers_inscritos, start=1):
        print(f"{i}. {camper['NombreCamper']}")

    while True:
        try:
            seleccion = int(input("Elija un Camper (0 para agregar uno nuevo): "))
            if 0 <= seleccion <= len(campers_inscritos):
                break
            else:
                mensajeError.msgError("Error \nSeleccion invalida, intentelo de nuevo")

        except ValueError:
            mensajeError.msgError("Error \nNumero invalido")

    if seleccion == 0:
        Campers.agregarCamper()
    else:
        camper_seleccionado = campers_inscritos[seleccion - 1]
        nota_teorica = float(
            input(
                f"Ingrese la Nota teorica para el estudiante {camper_seleccionado['NombreCamper']}: "
            )
        )
        nota_practica = float(
            input(
                f"Ingrese la Nota practica para el estudiante {camper_seleccionado['NombreCamper']}: "
            )
        )
        promedio = (nota_teorica + nota_practica) / 2

        if promedio >= 60:
            print("Aprobado")
            # Cambiar el estado del camper a "aprobado"
            camper_seleccionado["Estado"] = "aprobado"
        else:
            print("Reprobado")

        camper_seleccionado["NotaTeorica"] = nota_teorica
        camper_seleccionado["NotaPractica"] = nota_practica

        listasCampus.guardarCampers(mostrar_campers)


def asignarCamperaRuta():
    mostrar_campers = listasCampus.cargarCampers()

    # Filtrar campers aprobados
    campers_aprobados = [
        camper for camper in mostrar_campers if camper["Estado"].lower() == "aprobado"
    ]

    if not campers_aprobados:
        print("No hay campers aprobados para asignar a una ruta.")
        return

    # Mostrar campers aprobados para asignar
    print("Lista de campers aprobados disponibles:")
    for i, camper in enumerate(campers_aprobados, start=1):
        print(f"{i}. {camper['NombreCamper']}")

    while True:
        try:
            seleccion_camper = int(
                input("Seleccione un Camper (0 para volver atrás): ")
            )
            if 0 <= seleccion_camper <= len(campers_aprobados):  
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")

        except ValueError:
            mensajeError.msgError("Error: Número inválido")

    if seleccion_camper == 0:
        return  # Volver al menú anterior si el usuario selecciona 0

    camper_seleccionado = campers_aprobados[seleccion_camper - 1]

    # Mostrar las rutas disponibles
    rutas_disponibles = listasCampus.cargarRutas()

    if not rutas_disponibles:
        print("No hay rutas disponibles para asignar.")
        return

    print("Lista de rutas disponibles:")
    for ruta in rutas_disponibles:
        print(f"{ruta['CodigoRuta']}. {ruta['NombreRuta']}")

    while True:
        try:
            codigo_ruta = int(
                input("Seleccione una ruta por su código (0 para volver atrás): ")
            )
            if codigo_ruta == 0:
                return  # Volver al menú anterior si el usuario selecciona 0
            ruta_seleccionada = next(
                (
                    ruta
                    for ruta in rutas_disponibles
                    if ruta["CodigoRuta"] == codigo_ruta
                ),
                None,
            )
            if ruta_seleccionada:
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            mensajeError.msgError("Error: Código inválido")

    # Asignar la ruta al camper seleccionado
    camper_seleccionado["RutaAsignada"] = ruta_seleccionada["NombreRuta"]
    print(
        f"Ruta '{ruta_seleccionada['NombreRuta']}' asignada al camper '{camper_seleccionado['NombreCamper']}' con éxito."
    )
    listasCampus.guardarCampers(mostrar_campers)


# Función para asignar ruta y horario a un trainer
def asignarRutaTrainer():
    mostrar_trainers = listasCampus.cargarTrainers()

    # Mostrar lista de trainers
    print("Lista de trainers disponibles:")
    for i, trainer in enumerate(mostrar_trainers, start=1):
        print(f"{i}. {trainer['NombreTrainer']}")

    while True:
        try:
            seleccion_trainer = int(
                input("Seleccione un Trainer (0 para volver atrás): ")
            )
            if 0 <= seleccion_trainer <= len(mostrar_trainers):
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")

        except ValueError:
            mensajeError.msgError("Error: Número inválido")

    if seleccion_trainer == 0:
        return  # Volver al menú anterior si el usuario selecciona 0

    trainer_seleccionado = mostrar_trainers[seleccion_trainer - 1]

    # Mostrar las rutas disponibles
    rutas_disponibles = listasCampus.cargarRutas()

    if not rutas_disponibles:
        print("No hay rutas disponibles para asignar.")
        return

    print("Lista de rutas disponibles:")
    for ruta in rutas_disponibles:
        print(f"{ruta['CodigoRuta']}. {ruta['NombreRuta']}")

    while True:
        try:
            codigo_ruta = int(
                input("Seleccione una ruta por su código (0 para volver atrás): ")
            )
            if codigo_ruta == 0:
                return  # Volver al menú anterior si el usuario selecciona 0
            ruta_seleccionada = next(
                (
                    ruta
                    for ruta in rutas_disponibles
                    if ruta["CodigoRuta"] == codigo_ruta
                ),
                None,
            )
            if ruta_seleccionada:
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            mensajeError.msgError("Error: Código inválido")

    # Asignar la ruta al trainer seleccionado
    trainer_seleccionado["RutaAsignada"] = ruta_seleccionada["NombreRuta"]
    print(
        f"Ruta '{ruta_seleccionada['NombreRuta']}' asignada al trainer '{trainer_seleccionado['NombreTrainer']}' con éxito."
    )
    listasCampus.guardarTrainers(mostrar_trainers)
    
    # Cargar los horarios disponibles desde el archivo JSON
    with open("horario.json") as file:
        horarios = json.load(file)

    print("Lista de horarios disponibles:")
    for horario in horarios:
        print(f"{horario['Codigo']}. {horario['NombreJornada']} - {horario['Hora']['HoraInicio']} a {horario['Hora']['HoraFinal']}")

    while True:
        try:
            codigo_horario = int(
                input("Seleccione un horario por su código (0 para volver atrás): ")
            )
            if codigo_horario == 0:
                return  # Volver al menú anterior si el usuario selecciona 0
            horario_seleccionado = next(
                (
                    horario
                    for horario in horarios
                    if horario["Codigo"] == codigo_horario
                ),
                None,
            )
            if horario_seleccionado:
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            mensajeError.msgError("Error: Código inválido")

    trainer_seleccionado["HorarioAsignado"] = horario_seleccionado["NombreJornada"]
    print(f"Horario '{horario_seleccionado['NombreJornada']}' asignado al trainer '{trainer_seleccionado['NombreTrainer']}' con éxito.")

    # Guardar la información actualizada del trainer en el archivo JSON
    listasCampus.guardarTrainers(mostrar_trainers)
    mostrar_trainers = listasCampus.cargarTrainers()

    # Mostrar lista de trainers
    print("Lista de trainers disponibles:")
    for i, trainer in enumerate(mostrar_trainers, start=1):
        print(f"{i}. {trainer['NombreTrainer']}")

    while True:
        try:
            seleccion_trainer = int(
                input("Seleccione un Trainer (0 para volver atrás): ")
            )
            if 0 <= seleccion_trainer <= len(mostrar_trainers):
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")

        except ValueError:
            mensajeError.msgError("Error: Número inválido")

    if seleccion_trainer == 0:
        return  # Volver al menú anterior si el usuario selecciona 0

    trainer_seleccionado = mostrar_trainers[seleccion_trainer - 1]

    # Mostrar las rutas disponibles
    rutas_disponibles = listasCampus.cargarRutas()

    if not rutas_disponibles:
        print("No hay rutas disponibles para asignar.")
        return

    print("Lista de rutas disponibles:")
    for ruta in rutas_disponibles:
        print(f"{ruta['CodigoRuta']}. {ruta['NombreRuta']}")

    while True:
        try:
            codigo_ruta = int(
                input("Seleccione una ruta por su código (0 para volver atrás): ")
            )
            if codigo_ruta == 0:
                return  # Volver al menú anterior si el usuario selecciona 0
            ruta_seleccionada = next(
                (
                    ruta
                    for ruta in rutas_disponibles
                    if ruta["CodigoRuta"] == codigo_ruta
                ),
                None,
            )
            if ruta_seleccionada:
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            mensajeError.msgError("Error: Código inválido")

    # Asignar la ruta al trainer seleccionado
    trainer_seleccionado["RutaAsignada"] = ruta_seleccionada["NombreRuta"]
    print(
        f"Ruta '{ruta_seleccionada['NombreRuta']}' asignada al trainer '{trainer_seleccionado['NombreTrainer']}' con éxito."
    )
    listasCampus.guardarTrainers(mostrar_trainers)
    
    # Cargar los horarios disponibles desde el archivo JSON
    with open("horario.json") as file:
        horarios = json.load(file)

    print("Lista de horarios disponibles:")
    for horario in horarios:
        print(f"{horario['Codigo']}. {horario['NombreJornada']} - {horario['Hora']['HoraInicio']} a {horario['Hora']['HoraFinal']}")

    while True:
        try:
            codigo_horario = int(
                input("Seleccione un horario por su código (0 para volver atrás): ")
            )
            if codigo_horario == 0:
                return  # Volver al menú anterior si el usuario selecciona 0
            horario_seleccionado = next(
                (
                    horario
                    for horario in horarios
                    if horario["Codigo"] == codigo_horario
                ),
                None,
            )
            if horario_seleccionado:
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            mensajeError.msgError("Error: Código inválido")

    trainer_seleccionado["HorarioAsignado"] = horario_seleccionado["NombreJornada"]
    print(f"Horario '{horario_seleccionado['NombreJornada']}' asignado al trainer '{trainer_seleccionado['NombreTrainer']}' con éxito.")
    # Cargar las rutas disponibles
    rutas_disponibles = listasCampus.cargarRutas()
    if not rutas_disponibles:
        print("No hay rutas disponibles para asignar.")
        return

    print("Lista de rutas disponibles:")
    for ruta in rutas_disponibles:
        print(f"{ruta['CodigoRuta']}. {ruta['NombreRuta']}")

    while True:
        try:
            codigo_ruta = int(
                input("Seleccione una ruta por su código (0 para volver atrás): ")
            )
            if codigo_ruta == 0:
                return  # Volver al menú anterior si el usuario selecciona 0
            ruta_seleccionada = next(
                (
                    ruta
                    for ruta in rutas_disponibles
                    if ruta["CodigoRuta"] == codigo_ruta
                ),
                None,
            )
            if ruta_seleccionada:
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            mensajeError.msgError("Error: Código inválido")

    trainer["RutaAsignada"] = ruta_seleccionada["NombreRuta"]

    # Cargar los horarios disponibles desde el archivo JSON
    with open("horario.json") as file:
        horarios = json.load(file)

    print("Lista de horarios disponibles:")
    for horario in horarios:
        print(f"{horario['Codigo']}. {horario['NombreJornada']} - {horario['Hora']['HoraInicio']} a {horario['Hora']['HoraFinal']}")

    while True:
        try:
            codigo_horario = int(
                input("Seleccione un horario por su código (0 para volver atrás): ")
            )
            if codigo_horario == 0:
                return  # Volver al menú anterior si el usuario selecciona 0
            horario_seleccionado = next(
                (
                    horario
                    for horario in horarios
                    if horario["Codigo"] == codigo_horario
                ),
                None,
            )
            if horario_seleccionado:
                break
            else:
                mensajeError.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            mensajeError.msgError("Error: Código inválido")

    trainer["HorarioAsignado"] = horario_seleccionado["NombreJornada"]
    print(f"Ruta '{ruta_seleccionada['NombreRuta']}' y horario '{horario_seleccionado['NombreJornada']}' asignados al trainer '{trainer['NombreTrainer']}' con éxito.")
    listasCampus.guardarTrainers(mostrar_trainers)