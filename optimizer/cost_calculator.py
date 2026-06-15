def calcular_costo_total(
    distancia_total_km: float,
    destinos: list[dict],
    tipo_ruta: str = "libre"
) -> float:
    """
    Calcula el costo estimado del viaje.

    Este cálculo es aproximado y sirve para el MVP.
    Considera:
    - Gasolina
    - Casetas si la ruta es de peaje
    - Costo estimado por destino
    """

    precio_gasolina = 24.50
    rendimiento_auto = 13.0
    costo_caseta_por_km = 1.80

    litros_estimados = distancia_total_km / rendimiento_auto
    costo_gasolina = litros_estimados * precio_gasolina

    costo_casetas = 0.0

    if tipo_ruta.lower() in ["peaje", "cuota", "autopista"]:
        costo_casetas = distancia_total_km * costo_caseta_por_km

    costo_destinos = sum(
        float(destino.get("costo_estimado", 0))
        for destino in destinos
    )

    costo_total = costo_gasolina + costo_casetas + costo_destinos

    return round(costo_total, 2)


def calcular_tiempo_total(
    distancia_total_km: float,
    tipo_ruta: str = "libre"
) -> float:
    """
    Calcula el tiempo aproximado de traslado en horas.
    """

    velocidad_promedio = 80.0

    factor_tiempo = 1.25

    if tipo_ruta.lower() in ["peaje", "cuota", "autopista"]:
        factor_tiempo = 1.0

    tiempo = (distancia_total_km / velocidad_promedio) * factor_tiempo

    return round(tiempo, 2)