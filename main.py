import os
import menu
import Campers
import rutas
import Trainers
import mensajeError
import Asignaciones
import matriculas
import evaluarModulo
import camperRiesgo 
import reportes

def main():
    os.system("cls")  # Os es una libreria
    while True:
        op = menu.menuCampus()
        if op == 1:
            os.system("cls")
            Campers.menuCamper()
        elif op == 2:
            os.system("cls")
            Trainers.menuTrainer()
        elif op ==3:
            os.system("cls")
            rutas.rutasAgregadas()
        elif op == 4:
            os.system("cls")
            Asignaciones.menuAsignacion()
        elif op == 5:
            os.system("cls")
            matriculas.gestor_matriculas()
        elif op == 6:
            os.system("cls")
            evaluarModulo.evaluar_campers()
        elif op == 7:
            os.system("cls")
            camperRiesgo.campers_en_riesgo()
        elif op == 8:
            os.system("cls")
            reportes.menuReportes() 
        elif op == 9:
            salir = input("¿Está seguro que desea salir? (S/N): ")
            if salir.upper() == "S":
                print("\nGracias por usar el programa... Adiós...\n".center(80))
                break
            elif salir.upper() == "N":
                continue
            else:
                mensajeError.msgError("Error. Digite una opción válida.")
                continue

            
main()


