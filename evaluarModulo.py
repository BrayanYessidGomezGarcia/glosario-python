import matriculas
import mensajeError
import json


# Función para evaluar un módulo
def evaluar_modulo(camper, modulo):
    nota_teorica = float(input("Ingrese la nota teórica del camper para este módulo: "))
    nota_practica = float(
        input("Ingrese la nota práctica del camper para este módulo: ")
    )
    nota_quices = float(
        input("Ingrese la nota de los quices del camper para este módulo: ")
    )

    # Calcular la nota final con los pesos dados
    nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quices * 0.1)

    if nota_final >= 60:
        print(
            f"El camper {camper['NombreCamper']} ha aprobado el módulo {modulo['NombreModulo']} con una nota final de {nota_final}."
        )
        return True
    else:
        print(
            f"El camper {camper['NombreCamper']} no ha aprobado el módulo {modulo['NombreModulo']} con una nota final de {nota_final}."
        )
        return False


# Función para realizar la evaluación periódica de los campers
def evaluar_campers():
    # Cargar datos desde archivos JSON
    camper_data = matriculas.cargar_datos("camper.json")
    ruta_data = matriculas.cargar_datos("rutas.json")

    # Iterar sobre los campers
    for camper in camper_data:
        # Obtener la ruta de entrenamiento asignada al camper
        ruta_asignada = next(
            (
                ruta
                for ruta in ruta_data
                if ruta["NombreRuta"] == camper["RutaAsignada"]
            ),
            None,
        )
        if ruta_asignada:
            print(
                f"\nEvaluación de camper: {camper['NombreCamper']} {camper['ApellidoCamper']}"
            )
            mensajeError.msgError("Error de ruta")

        # Iterar sobre los módulos de la ruta asignada
        for modulo in ruta_asignada["Modulos"]:
            print(f"\nEvaluación del módulo: {modulo['NombreModulo']}")
            # Evaluar el módulo para el camper
            if evaluar_modulo(camper, modulo):
                # Verificar si existe la clave 'Modulos_aprobados' en el camper
                if "Modulos_aprobados" not in camper:
                    camper["Modulos_aprobados"] = []
                camper["Modulos_aprobados"].append(modulo["NombreModulo"])

    # Actualizar el archivo JSON de campers con los módulos aprobados
    with open("camper.json", "w") as file:
        json.dump(camper_data, file, indent=2)
