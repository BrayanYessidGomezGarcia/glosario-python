import matriculas

# Función para identificar campers en riesgo
def campers_en_riesgo():
    # Cargar datos de los campers desde el archivo JSON
    camper_data = matriculas.cargar_datos('camper.json')
    ruta_data = matriculas.cargar_datos('rutas.json')

    # Lista para almacenar campers en riesgo
    campers_riesgo = []

    # Iterar sobre los campers
    for camper in camper_data:
        # Obtener la ruta de entrenamiento asignada al camper
        ruta_asignada = next((ruta for ruta in ruta_data if ruta['NombreRuta'] == camper['RutaAsignada']), None)
        if ruta_asignada:
            # Iterar sobre los módulos de la ruta asignada
            for modulo in ruta_asignada['Modulos']:
                # Verificar si el camper tiene una nota inferior a 60 en algún módulo
                if 'Notas' in camper and camper['Notas'].get(modulo['NombreModulo'], 0) < 60:
                    campers_riesgo.append(camper)
                    break  # Salir del bucle si se encuentra un módulo con nota inferior a 60

    # Mostrar campers en riesgo
    if campers_riesgo:
        print("\nCampers en riesgo:")
        for camper in campers_riesgo:
            print(f"{camper['NombreCamper']} {camper['ApellidoCamper']} - Ruta: {camper['RutaAsignada']}")
    else:
        print("\nNo hay campers en riesgo.")