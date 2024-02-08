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
        promedio_filtro= (nota_teorica + nota_practica)/2 

        if promedio_filtro >= 60:
            print("Filtro Aprobado")
        else:
            print("Filtro Reprobado")


        camper_seleccionado['NotaTeorica'] = nota_teorica
        camper_seleccionado['NotaPractica'] = nota_practica

        listasCampus.guardarCampers(mostrar_campers)    


def notasActividades():
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
        
        print("Ingrese las notas de las actividades: ")
        nota1= float(input("Ingrese 1. Nota: "))
        nota2= float(input("Ingrese 1. Nota: "))
        nota3= float(input("Ingrese 1. Nota: "))
        promedio_t= (nota1+nota2+nota3)/3

        if promedio_t >= 60:
            print("Notas en Actividades Aprobado")
        else:
            print("Notas en Actividades Reprobado")


        print("Ingrese Nota del Quiz: ")
        nota_filtro= float(input("Ingrese Nota: "))
                
        if nota_filtro >= 60:
            print("Quiz Aprobado")
        else:
            print("Quiz Reprobado")
        
        
           
        print("Ingrese Nota del Proyecto: ")
        nota_proyecto= float(input("Ingrese Nota: "))
                    
        if nota_proyecto >= 60:
            print("Proyecto Aprobado")
        else:
            print("Proyecto Reprobado")

        promedio= (promedio_t+nota_filtro+nota_proyecto)/3

        if promedio >= 60:
            print("Camper Aprobado")
        else:
            print("Camper Reprobado")



def menu():
    bandera=True 
    while (bandera):
        print("\t.1 Notas Filtro ")
        print("\t.2 Notas Actividades  ")
        opc = int(input("Ingrese una Opcion:"))
        match(opc):
             case 1: NotasAsignadas()
             case 2: notasActividades()



                

                

        
        

    

