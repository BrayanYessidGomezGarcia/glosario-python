import listasCampus
import Campers
import mensajeError

def NotasAsignadas():
    mostrar_campers= listasCampus.cargarCampers()
    campers_inscritos= [camper for camper in mostrar_campers
                            if camper['Estado'].lower()=="inscrito"]
    if not mostrar_campers:
        print("No hay camper registrado. Por favor agregue uno")
        Campers.agregarCamper()
        return
    
    print("Lista de campers en estado de inscritos")
    for i,camper in enumerate(campers_inscritos,start=1): 
        print(f"{i}. {camper['NombreCamper']}")

    while True:
        try: 
            seleccion= int(input("Elija un Camper (0 para agregar uno nuevo): "))
            if 0 <= seleccion <= len(campers_inscritos):
                break 
            else:
                mensajeError.msgError("Error \nSeleccion invalida, intentelo de nuevo")
            
        except ValueError:
            mensajeError.msgError("Error \nNumero invalido")

    if seleccion == 0: 
        Campers.agregarCamper()
    else:
        camper_seleccionado= campers_inscritos[seleccion-1]
        nota_teorica= float(input(f"Ingrese la Nota teorica para el estudiante {camper_seleccionado['NombreCamper']}: "))
        nota_practica= float(input(f"Ingrese la Nota practica para el estudiante {camper_seleccionado['NombreCamper']}: "))
        promedio= (nota_teorica + nota_practica)/2 

        if promedio >= 60:
            print("Aprobado")
        else:
            print("Reprobado")

        camper_seleccionado['NotaTeorica'] = nota_teorica
        camper_seleccionado['NotaPractica'] = nota_practica

        listasCampus.guardarCampers(mostrar_campers)    



