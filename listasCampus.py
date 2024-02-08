import json

CAMPERS_FILE = "camper.json"
RUTAS_FILE = "rutas.json"
HORARIO_FILE = "horario.json"
TRAINERS_FILE= "trainers.json"

def cargarCampers():
    try:
        with open(CAMPERS_FILE, 'r') as fileCamper:
            campers = json.load(fileCamper)

    except FileNotFoundError:
        campers = []
    return campers    

def guardarCampers(campers):
    with open(CAMPERS_FILE, 'w') as fileCamper:
        json.dump(campers, fileCamper, indent=2)


def cargarRutas():
    try:
        with open(RUTAS_FILE, 'r') as fileRutas:
            rutas= json.load(fileRutas)
        
    except FileNotFoundError: 
        rutas = []
    return rutas

def guardarRutas(rutas):
    with open(RUTAS_FILE, 'w') as fileRutas:
        json.dump(rutas,fileRutas, indent=2)


def cargarHorarios():
    try:
        with open(HORARIO_FILE, 'r') as fileHorario:
            horario = json.load(fileHorario)

    except FileNotFoundError:
        horario = []
    return horario    

def guardarHorarios(horario):
    with open(HORARIO_FILE, 'w') as horario_file:
        json.dump(horario, horario_file, indent=2)


def cargarTrainers():
    try: 
        with open (TRAINERS_FILE, 'r') as trainers_file:
            trainers= json.load(trainers_file)
        
    except FileNotFoundError:
        trainers= []
    return trainers

def guardarTrainers(trainers): 
    with open(TRAINERS_FILE, 'w') as trainers_file:
        json.dump(trainers, trainers_file, indent=2 )





