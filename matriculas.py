import json
from datetime import datetime, timedelta

# Cargar datos desde los archivos JSON
def cargar_datos(archivo):
    with open(archivo, 'r') as file:
        return json.load(file)

# Función para guardar la información de la matrícula en un archivo JSON
def guardar_matricula(matricula):
    with open('matriculas.json', 'a') as file:
        json.dump(matricula, file, indent=2)
        file.write('\n')  # Agregar nueva línea después de cada matrícula

# Función para asignar un camper a una ruta de entrenamiento, un trainer y un salón
def asignar_matricula(camper, ruta, trainer, salon):
    # Generar fechas de inicio y finalización
    fecha_inicio = datetime.now().strftime('%Y-%m-%d')
    fecha_finalizacion = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

    # Mostrar la información de la matrícula
    matricula = {
        "Camper": f"{camper['NombreCamper']} {camper['ApellidoCamper']}",
        "Ruta_de_entrenamiento": ruta['NombreRuta'],
        "Trainer": trainer['NombreTrainer'],
        "Salon": salon['NombreSala'],
        "Fecha_de_inicio": fecha_inicio,
        "Fecha_de_finalizacion": fecha_finalizacion
    }

    print("\nMatrícula asignada:")
    print(json.dumps(matricula, indent=2))

    # Guardar la matrícula en un archivo JSON
    guardar_matricula(matricula)

# Función principal del gestor de matrículas
def gestor_matriculas():
    # Cargar datos desde archivos JSON
    camper_data = cargar_datos('camper.json')
    ruta_data = cargar_datos('rutas.json')
    trainer_data = cargar_datos('trainers.json')
    salon_data = cargar_datos('salones.json')

    # Verificar si hay campers aprobados
    campers_aprobados = [camper for camper in camper_data if camper['Estado'] == 'aprobado']

    # Verificar si hay rutas disponibles
    if not campers_aprobados:
        print("No hay campers aprobados para matricular.")
        return

    # Asignar la matrícula a cada camper, siguiendo el orden
    for i, camper in enumerate(campers_aprobados):
        ruta = ruta_data[i % len(ruta_data)]  # Tomar la ruta siguiente en la lista, ciclando si es necesario
        trainer = trainer_data[i % len(trainer_data)]  # Tomar el siguiente trainer en la lista, ciclando si es necesario
        salon = salon_data[i % len(salon_data)]  # Tomar el siguiente salón en la lista, ciclando si es necesario
        asignar_matricula(camper, ruta, trainer, salon)