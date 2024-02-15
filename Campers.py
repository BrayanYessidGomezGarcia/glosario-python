import mensajeError
import listasCampus
import os


def menuCamper():
    while True:
        try:
            print("\n\n**CRUD DE CAMPERS**")
            print("\tMENU")
            print("1. Agregar Camper")
            print("2. Modificar Camper")
            print("3. Buscar Camper")
            print("4. Eliminar Camper")
            print("5. Salir")
            op = int(input("\t>>Escoja una opcion (1-5): "))
            if op < 1 or op > 5:
                mensajeError.msgError("Error. Opcion Invalida (de 1 a 5)")
                continue
            if op == 1:
                os.system("cls")
                agregarCamper()
                input("Presione enter para volver al menu")
            elif op == 2:
                os.system("cls")
                nombre_a_modificar =input("Ingrese el nombre del camper que desea modificar: ")
                editarCamper(nombre_a_modificar)
                input("Presione enter para volver al menu")
            elif op == 3:
                os.system("cls")
                buscarCamper()
                input("Presione enter para volver al menu")
            elif op == 4:
                os.system("cls")
                eliminarCamper()
                input("Presione enter para volver al menu")
            elif op == 5:
                os.system("cls")
                eliminarCamper()
                input("Presione enter para volver al menu")
            elif op == 6:
                os.system("cls")
                break
            return op

        except ValueError:
            mensajeError.msgError("Error. Opcion Invalida (de 1 a 5)")
            continue


# Funcion para agregar un camper
def agregarCamper():
    print("AGREGAR CAMPER")

    id_camper = None
    while id_camper is None:
        try:
            id_camper = int(input("Ingrese numero de Identificacion: "))
        except ValueError:
            mensajeError.msgError("Numero invalido")

    nombre_camper = input("Ingrese su Nombre: ")
    while not nombre_camper:
        mensajeError.msgError("El nombre no puede estar vacio")
        nombre_camper = input("Ingrese Nombres: ")

    apellido_camper = input("Ingrese Apellidos: ")
    while not apellido_camper:
        mensajeError.msgError("El Apellido no puede estar vacio")
        apellido_camper = input("Ingrese Apellidos: ")

    tel_celular = None
    while tel_celular is None:
        try:
            tel_celular = int(input("Ingrese su numero celular: "))
        except ValueError:
            mensajeError.msgError("Numero no valido")

    tel_fijo = None
    while tel_fijo is None:
        try:
            tel_fijo = int(input("Ingrese numero fijo de contacto: "))
        except ValueError:
            mensajeError.msgError("Numero no valido")

    estado = input("Ingrese estado: ")
    while not estado:
        mensajeError.msgError("El estado no puede estar vacio")
        estado = input("Ingrese estado: ")

    camper_diccionario = {
        "IdentificacionCamper": id_camper,
        "NombreCamper": nombre_camper,
        "ApellidoCamper": apellido_camper,
        "TelContacto": {"telefonoCelular": tel_celular, "telefonoFijo": tel_fijo},
        "Estado": estado,
    }

    listCamper = listasCampus.cargarCampers()
    listCamper.append(camper_diccionario)
    listasCampus.guardarCampers(listCamper)
    print("Camper Agregado Exitosamente")


# Funcion para listar campers
def mostrarListaCampers():
    campers = listasCampus.cargarCampers()
    print("Lista de Campers:")
    for index, camper in enumerate(campers, start=1):
        print(f"{index}. {camper['NombreCamper']} {camper['ApellidoCamper']}")


# Funcion para modificar un camper
def editarCamper(nombre_a_modificar):
    print("MODIFICAR CAMPER")
    listCamper = listasCampus.cargarCampers()
    encontrado = False
    for camper in listCamper:
        if camper["NombreCamper"] == nombre_a_modificar:
            print(f"Camper encontrado: {camper}")

            camper["NombreCamper"] = input("Nuevo nombre: ")
            while not camper["NombreCamper"]:
                mensajeError.msgError("El nombre no puede estar vacio")
                camper["NombreCamper"] = input("Nuevo nombre: ")

            camper["ApellidoCamper"] = input("Nuevo apellido: ")
            while not camper["ApellidoCamper"]:
                mensajeError.msgError("El Apellido no puede estar vacio")
                camper["ApellidoCamper"] = input("Nuevo apellido")

            tel_celular = None
            while tel_celular is None:
                try:
                    tel_celular = int(input("Nuevo numero de celular: "))
                except ValueError:
                    mensajeError.msgError("Numero no valido")
            camper["TelContacto"]["telefonoCelular"] = tel_celular

            tel_fijo = None
            while tel_fijo is None:
                try:
                    tel_fijo = int(input("Nuevo numero fijo: "))
                except ValueError:
                    mensajeError.msgError("Telefono de contacto Invalido")
            camper["TelContacto"]["telefonoFijo"] = tel_fijo
            break

    if encontrado:
        listasCampus.guardarCampers(listCamper)
        print("Camper modificado exitosamente.")
    else:
        print("Camper no encontrado.")


# Funcion para Buscar un Camper
def buscarCamper():
    print("BUSCAR CAMPER: ")
    campers = listasCampus.cargarCampers()
    nombre_buscar = input("Ingrese el nombre del camper que desea buscar: ")
    encontrado = False
    for camper in campers:
        if camper["NombreCamper"] == nombre_buscar:
            encontrado = True
            print("Camper encontrado:")
            print(f"Identificacion: {camper['IdentificacionCamper']}")
            print(f"Nombre: {camper['NombreCamper']} {camper['ApellidoCamper']}")
            print(f"Direccion: {camper['DireccionCamper']}")
            print(
                f"Nombre del Acudiente: {camper['AcudienteCamper']['NombreAcudiente']}"
            )
            print(
                f"Identificacion del Acudiente: {camper['AcudienteCamper']['IdAcudiente']}"
            )
    if not encontrado:
        print("Camper no encontrado.")


# Funcion para eliminar un camper
def eliminarCamper():
    print("ELIMINAR CAMPER")
    campers = listasCampus.cargarCampers()
    mostrarListaCampers()

    nombre_eliminar = input("Ingrese el nombre del camper que desea eliminar: ")

    encontrado = False
    for index, camper in enumerate(campers):
        if camper["NombreCamper"] == nombre_eliminar:
            encontrado = True
            # Mostrar los detalles del camper encontrado
            print("Camper encontrado:")
            print(f"Identificacion: {camper['IdentificacionCamper']}")
            print(f"Nombre: {camper['NombreCamper']} {camper['ApellidoCamper']}")
            print(f"Direccion: {camper['DireccionCamper']}")
            print(
                f"Nombre del Acudiente: {camper['AcudienteCamper']['NombreAcudiente']}"
            )
            print()
            confirmacion = input(
                "¿Está seguro de que desea eliminar este camper? (s/n): "
            ).lower()
            if confirmacion == "s":
                del campers[index]
                listasCampus.guardarCampers(campers)
                print("Camper eliminado exitosamente.")
                os.system("cls")
            else:
                print("Operación cancelada.")
                os.system("cls")
            break

    if not encontrado:
        print("Camper no encontrado.")


def campersRiesgo():
    print("**CAMPERS EN RIESGO BAJO**")
    campers = listasCampus.cargarCampers
