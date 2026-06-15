import random

from optimizer.distance_calculator import calcular_distancia_ruta


def crear_individuo(destinos: list[dict], cantidad_destinos: int) -> list[dict]:
    """
    Crea una posible ruta seleccionando destinos aleatorios.
    """

    cantidad = min(cantidad_destinos, len(destinos))
    return random.sample(destinos, cantidad)


def calcular_fitness(origen: dict, individuo: list[dict]) -> float:
    """
    Evalúa qué tan buena es una ruta.
    En este MVP, menor distancia significa mejor fitness.
    """

    distancia = calcular_distancia_ruta(origen, individuo)
    return distancia


def cruzar_padres(
    padre_1: list[dict],
    padre_2: list[dict],
    destinos_disponibles: list[dict],
    cantidad_destinos: int
) -> list[dict]:
    """
    Cruza dos rutas para generar una nueva ruta hija.
    Evita repetir destinos.
    """

    hijo = []

    mitad = len(padre_1) // 2

    for destino in padre_1[:mitad]:
        if destino not in hijo:
            hijo.append(destino)

    for destino in padre_2:
        if destino not in hijo and len(hijo) < cantidad_destinos:
            hijo.append(destino)

    while len(hijo) < cantidad_destinos:
        destino_extra = random.choice(destinos_disponibles)

        if destino_extra not in hijo:
            hijo.append(destino_extra)

    return hijo


def mutar_individuo(
    individuo: list[dict],
    destinos_disponibles: list[dict],
    probabilidad_mutacion: float = 0.15
) -> list[dict]:
    """
    Aplica una pequeña modificación a la ruta.
    Puede intercambiar el orden de visita o reemplazar un destino.
    """

    nuevo_individuo = individuo.copy()

    if random.random() < probabilidad_mutacion and len(nuevo_individuo) > 1:
        indice_1 = random.randint(0, len(nuevo_individuo) - 1)
        indice_2 = random.randint(0, len(nuevo_individuo) - 1)

        nuevo_individuo[indice_1], nuevo_individuo[indice_2] = (
            nuevo_individuo[indice_2],
            nuevo_individuo[indice_1]
        )

    if random.random() < probabilidad_mutacion:
        indice = random.randint(0, len(nuevo_individuo) - 1)
        nuevo_destino = random.choice(destinos_disponibles)

        if nuevo_destino not in nuevo_individuo:
            nuevo_individuo[indice] = nuevo_destino

    return nuevo_individuo


def optimizar_ruta_genetico(
    origen: dict,
    destinos: list[dict],
    cantidad_destinos: int = 3,
    generaciones: int = 120,
    tamano_poblacion: int = 50,
    probabilidad_mutacion: float = 0.15
) -> dict:
    """
    Optimiza una ruta turística mediante un algoritmo genético simple.

    Entrada:
    - Origen
    - Lista de destinos candidatos
    - Cantidad de destinos a visitar

    Salida:
    - Mejor ruta encontrada
    - Distancia total aproximada
    """

    if not destinos:
        return {
            "ruta": [],
            "distancia_total_km": 0.0
        }

    cantidad_destinos = min(cantidad_destinos, len(destinos))

    poblacion = [
        crear_individuo(destinos, cantidad_destinos)
        for _ in range(tamano_poblacion)
    ]

    for _ in range(generaciones):
        poblacion_ordenada = sorted(
            poblacion,
            key=lambda individuo: calcular_fitness(origen, individuo)
        )

        mejores = poblacion_ordenada[:tamano_poblacion // 2]

        nueva_poblacion = mejores.copy()

        while len(nueva_poblacion) < tamano_poblacion:
            padre_1 = random.choice(mejores)
            padre_2 = random.choice(mejores)

            hijo = cruzar_padres(
                padre_1,
                padre_2,
                destinos,
                cantidad_destinos
            )

            hijo = mutar_individuo(
                hijo,
                destinos,
                probabilidad_mutacion
            )

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    mejor_ruta = min(
        poblacion,
        key=lambda individuo: calcular_fitness(origen, individuo)
    )

    distancia_total = calcular_distancia_ruta(origen, mejor_ruta)

    return {
        "ruta": mejor_ruta,
        "distancia_total_km": distancia_total
    }