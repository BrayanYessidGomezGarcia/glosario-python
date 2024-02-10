import listasCampus
import Campers
import mensajeError
import rutas

def asignarCamperXRuta():
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
        rutas.listarRutas()
        while True:
            try:
                seleccion = int(input("Elija una ruta para asignar: "))
                break
            except ValueError:
                mensajeError.msgError("Error \nNumero Invalido")
        
                  