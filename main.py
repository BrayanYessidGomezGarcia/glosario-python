import os
import menu
import Campers
import asignarNotas
import agregarRutas
import agregarHorario
import agregarTrainer

def main():
    os.system("cls")  # Os es una libreria
    while True:
        op = menu.menuCampus()
        if op == 1:
            os.system("cls")
            Campers.menuCamper()
        if op == 2:
            os.system("cls")
            asignarNotas.menu()
        if op ==3:
            os.system("cls")
            agregarRutas.rutasAgregadas()
        if op == 4:
            os.system("cls")
            agregarHorario.horarioAgregado()
        
        if op == 5:
            os.system("cls")
            agregarTrainer.trainerAgregado()

            
main()


