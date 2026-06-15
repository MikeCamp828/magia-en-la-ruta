from math import radians, sin, cos, sqrt, atan2


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calcula la distancia aproximada en kilómetros entre dos puntos geográficos
    usando la fórmula Haversine.
    """

    radio_tierra_km = 6371.0

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    diferencia_lat = lat2_rad - lat1_rad
    diferencia_lon = lon2_rad - lon1_rad

    a = (
        sin(diferencia_lat / 2) ** 2
        + cos(lat1_rad) * cos(lat2_rad) * sin(diferencia_lon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return round(radio_tierra_km * c, 2)


def calcular_distancia_ruta(origen: dict, destinos: list[dict]) -> float:
    """
    Calcula la distancia total aproximada de una ruta.
    La ruta inicia en el origen y visita los destinos en el orden recibido.
    """

    if not destinos:
        return 0.0

    distancia_total = 0.0

    lat_actual = origen["latitud"]
    lon_actual = origen["longitud"]

    for destino in destinos:
        distancia = haversine_distance(
            lat_actual,
            lon_actual,
            destino["latitud"],
            destino["longitud"]
        )

        distancia_total += distancia

        lat_actual = destino["latitud"]
        lon_actual = destino["longitud"]

    return round(distancia_total, 2)