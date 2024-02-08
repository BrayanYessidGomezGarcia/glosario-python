import mensajeError
import listasCampus

def rutasAgregadas():
    print("AGREGAR RUTAS DE ENTRENAMIENTO")
    cantidad_rutas= int(input("Cuantas rutas desea agregar: "))

    while cantidad_rutas <= 0:
        mensajeError.msgError("Agregar al menos una ruta de entrenamiento")
        cantidad_rutas= int(input("Cuantas rutas desea agregar: "))
    
    for i in range(1,cantidad_rutas +1):
        print(f"Ruta {i}")

        nombre_ruta= input("Ingrese el Nombre de la Ruta: ")
        while not nombre_ruta:
            mensajeError.msgError("El nombre no puede estar vacio")
            nombre_ruta=input("Ingrese el nombre de la Ruta")
        
        cantidad_modulos= int(input("Ingrese la cantidad de modulos: "))
        while cantidad_modulos <= 0: 
            mensajeError.msgError("Agregar al menos un modulo")
            cantidad_modulos=int(input("Ingrese la cantidad de modulos "))

        for i in range(1,cantidad_modulos +1):
            print(f"Modulo {i}")

            nombre_modulo= input(f"Ingrese el nombre del Modulo de la ruta {nombre_ruta}: ")
            while not nombre_modulo:
                mensajeError.msgError("El nombre del modulo no puede estar vacio")
                nombre_modulo= input (f"Ingrese el nombre del Modulo de la ruta {nombre_ruta}: ")
            
          
            codigo_modulo= None
            while codigo_modulo is None: 
                try: 
                    codigo_modulo= int(input("Ingrese el codigo del Modulo: "))
                except ValueError:
                    mensajeError.msgError("Numero Invalido")

            cantidad_temas= int(input("Ingrese la cantidad de temas: "))
            while cantidad_temas <= 0: 
                mensajeError.msgError("Agregar al menos un tema")
                cantidad_temas= int(input("Ingrese la cantidad de temas: "))
            
            for i in range(1, cantidad_temas +1):
                print(f"Tema {i}")
            
            temarios= input("Ingrese el nombre del Tema: ")
            while not temarios:
                mensajeError.msgError("El nombre del Tema no puede estar Vacio")
                temarios=  input("Ingrese el nombre del Tema: ")
            
        codigo_ruta= None 
        while codigo_ruta is None:
            try: 
                codigo_ruta= int(input("Ingrese el codigo de Ruta: "))
            except ValueError:
                mensajeError.msgError("Codigo Invalido")


    rutas_Diccionario= {
        "NombreRuta": nombre_ruta,
        "Modulos": {
            "NombreModulo":  nombre_modulo,
            "CodigoModulo": codigo_modulo,
            "Temas": {
                "NombreTema": temarios
            } 
        },
        "CodigoRuta": codigo_ruta
    }

    lista_ruta= listasCampus.cargarRutas()
    lista_ruta.append(rutas_Diccionario)
    listasCampus.guardarRutas(lista_ruta)




