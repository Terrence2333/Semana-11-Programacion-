def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad a partir de los datos semanales y diarias.

    Parámetros:
    datos_temperaturas (dict): Un diccionario donde las claves son los nombres de las ciudades y los valores
                               son listas de listas con las temperaturas registradas en cada día de la semana por semana.

    Retorna:
    dict: Un diccionario con el promedio de temperatura de cada ciudad.
    """
    promedios = {}
    for ciudad, semanas in datos_temperaturas.items():
        temperaturas_totales = [temp for semana in semanas for temp in semana]
        promedio = sum(temperaturas_totales) / len(temperaturas_totales) if temperaturas_totales else 0
        promedios[ciudad] = round(promedio, 2)

    return promedios


# Datos de ejemplo: temperaturas de 3 ciudades durante 4 semanas y 7 días por semana
datos_temperaturas = {
    "Moscú": [
        [30, 32, 31, 29, 28, 30, 31],
        [31, 33, 30, 29, 30, 32, 33],
        [30, 29, 28, 27, 29, 30, 31],
        [32, 31, 30, 29, 28, 27, 26]
    ],
    "New York": [
        [25, 26, 27, 24, 23, 25, 26],
        [26, 27, 28, 25, 24, 26, 27],
        [27, 28, 26, 24, 25, 27, 28],
        [24, 25, 26, 23, 22, 24, 25]
    ],
    "Quito": [
        [20, 21, 22, 19, 18, 20, 21],
        [21, 22, 23, 20, 19, 21, 22],
        [22, 23, 21, 19, 20, 22, 23],
        [19, 20, 21, 18, 17, 19, 20]
    ]
}

# Llamamos a la función y mostramos los resultados
resultados = calcular_temperatura_promedio(datos_temperaturas)
print("Temperaturas promedio por ciudad (°C):")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}°C")
