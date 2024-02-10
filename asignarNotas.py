import listasCampus
import Campers
import mensajeError

#Funcion para sacar Notas del filtro
def NotasAsignadas():
    mostrar_campers = listasCampus.cargarCampers()
    campers_inscritos = [camper for camper in mostrar_campers
                         if camper['Estado'].lower() == "inscrito"]
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
        nota_teorica = float(input(f"Ingrese la Nota teorica para el estudiante {camper_seleccionado['NombreCamper']}: "))
        nota_practica = float(input(f"Ingrese la Nota practica para el estudiante {camper_seleccionado['NombreCamper']}: "))
        notasActividades(nota_teorica, nota_practica)  # Pasar ambas notas como argumentos

        promedio_filtro = (nota_teorica + nota_practica) / 2

        if promedio_filtro >= 60:
            print("Filtro Aprobado")
        else:
            print("Filtro Reprobado")

        camper_seleccionado['NotaTeorica'] = nota_teorica
        camper_seleccionado['NotaPractica'] = nota_practica

        listasCampus.guardarCampers(mostrar_campers)


#Funcion para sacar Notas
def notasActividades(nota_teorica, nota_practica): 

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
        nota_quiz= float(input("Ingrese Nota: "))
                
        if nota_quiz >= 60:
            print("Quiz Aprobado")
        else:
            print("Quiz Reprobado")
        
        
           
        print("Ingrese Nota del Proyecto: ")
        nota_proyecto= float(input("Ingrese Nota: "))
                    
        if nota_proyecto >= 60:
            print("Proyecto Aprobado")
        else:
            print("Proyecto Reprobado")

        promedio= (promedio_t+nota_quiz+nota_proyecto)/3

        if promedio >= 60:
            print("Camper Aprobado")
        else:
            print("Camper Reprobado")


    notas_diccionario= {
        "NotaFiltro": {
            "NotaTeorica": nota_teorica,
            "NotaPractica": nota_practica,
        },
        "NotaActividades":  promedio_t,
        "NotaQuiz": nota_quiz,
        "NotaProyecto": nota_proyecto
    }

    lista_notas= listasCampus.cargarNotas()
    lista_notas.append(notas_diccionario)
    listasCampus.guardarNotas(lista_notas)

                

                

        
        

    

