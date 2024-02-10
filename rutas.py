import mensajeError
import listasCampus

def rutasAgregadas():
    print("AGREGAR RUTAS DE ENTRENAMIENTO")
    
    cantidad_rutas = int(input("Ingrese la cantidad de rutas que desea agregar: "))
    while cantidad_rutas <= 0:
        mensajeError.msgError("¡Debe ingresar al menos una ruta de entrenamiento!")
        cantidad_rutas = int(input("Ingrese la cantidad de rutas que desea agregar: "))

    listaRutas = []  # Inicializamos una lista vacía para almacenar las rutas

    for i in range(1, cantidad_rutas + 1):
        print(f"\nRuta {i}")
        
        codigo_ruta = None
        while codigo_ruta is None:
            try:
                codigo_ruta = int(input("Ingrese el codigo de la ruta: "))
            except ValueError:
                mensajeError.msgError("Numero no valido")    
            
        nombre_ruta = input("Escriba el nombre de la ruta de entrenamiento: ")
        while not nombre_ruta:
            mensajeError.msgError("¡El nombre no puede estar vacío!")
            nombre_ruta = input("Escriba el nombre de la ruta de entrenamiento: ")

        cantidad_modulos = int(input("Ingrese la cantidad de modulos que desea agregar: "))
        while cantidad_modulos <= 0:
            mensajeError.msgError("¡Debe ingresar al menos un modulo!")
            cantidad_modulos = int(input("Ingrese la cantidad de modulos que desea agregar: "))

        modulos = []  # Inicializamos una lista vacía para almacenar los módulos de cada ruta

        for j in range(1, cantidad_modulos + 1):
            print(f"\nModulo {j}")

            codigo_modulo = None
            while codigo_modulo is None:
                try:
                    codigo_modulo = int(input(f"Escriba el codigo del modulo: "))
                except ValueError:
                    mensajeError.msgError("¡El codigo debe ser un número valido!")    
                    
            nombre_modulo = input(f"Escriba el nombre del modulo de la ruta {nombre_ruta}: ")
            while not nombre_modulo:
                mensajeError.msgError("¡El nombre no puede estar vacío!")
                nombre_modulo = input(f"Escriba el nombre del modulo de la ruta {nombre_ruta}: ")

            cantidad_temas = int(input(f"Ingrese la cantidad de temas para el modulo {nombre_modulo}: "))
            while cantidad_temas <= 0:
                mensajeError.msgError("¡Debe ingresar al menos un tema!")
                cantidad_temas = int(input(f"Ingrese la cantidad de temas para el modulo {nombre_modulo}: "))
            
            temas = []  # Inicializamos una lista vacía para almacenar los temas de cada módulo

            for k in range(1, cantidad_temas + 1):
                nombre_tema = input(f"Escriba el nombre del tema {k} del modulo {nombre_modulo}: ")
                while not nombre_tema:
                    mensajeError.msgError("¡El nombre no puede estar vacío!")
                    nombre_tema = input(f"Escriba el nombre del tema {k} del modulo {nombre_modulo}: ")
                
                # Agregamos el tema a la lista de temas
                temas.append({"NombreTema": nombre_tema})

            # Agregamos el módulo con sus temas a la lista de módulos
            modulos.append({
                "CodigoModulo": codigo_modulo,
                "NombreModulo": nombre_modulo,
                "Temas": temas
            })

        # Agregamos la ruta con sus módulos a la lista de rutas
        listaRutas.append({
            "CodigoRuta": codigo_ruta,
            "NombreRuta": nombre_ruta,
            "Modulos": modulos
        })

    # Guardamos la lista de rutas en el archivo de datos
    listasCampus.guardarRutas(listaRutas)
 
 
def listarRutas():
    # Cargar la lista de rutas
    rutas = listasCampus.cargarRutas()

    # Verificar si hay rutas disponibles
    if not rutas:
        print("No hay rutas disponibles.")
        return

    print("\nLISTA DE RUTAS DE ENTRENAMIENTO:")
    for ruta in rutas:
        print(f"\nRuta {ruta['CodigoRuta']}: {ruta['NombreRuta']}")
        print("Modulos:")
        for modulo in ruta['Modulos']:
            print(f"  - Módulo {modulo['CodigoModulo']}: {modulo['NombreModulo']}")
            print("    Temas:")
            for tema in modulo['Temas']:
                print(f"      * {tema['NombreTema']}")    
