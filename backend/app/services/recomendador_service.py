from decimal import Decimal
from pathlib import Path
import sys

from sqlalchemy.orm import Session

from app.models.destino_model import Destino
from app.schemas.recomendacion_schema import RecomendacionRequest


# Permite importar la carpeta optimizer desde la raíz del proyecto.
PROJECT_ROOT = Path(__file__).resolve().parents[3]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from optimizer.distance_calculator import haversine_distance


def convertir_decimal(valor):
    """
    Convierte valores Decimal de PostgreSQL a float.
    """

    if isinstance(valor, Decimal):
        return float(valor)

    return valor


def convertir_destino_a_dict(destino: Destino) -> dict:
    """
    Convierte un objeto Destino de SQLAlchemy a diccionario.
    """

    return {
        "id_destino": destino.id_destino,
        "nombre": destino.nombre,
        "estado": destino.estado,
        "tipo": destino.tipo,
        "descripcion": destino.descripcion,
        "latitud": convertir_decimal(destino.latitud),
        "longitud": convertir_decimal(destino.longitud),
        "costo_estimado": convertir_decimal(destino.costo_estimado),
        "tiempo_visita_horas": convertir_decimal(destino.tiempo_visita_horas),
        "intereses": destino.intereses,
        "imagen_url": destino.imagen_url
    }


def calcular_puntaje_destino(
    destino: dict,
    solicitud: RecomendacionRequest,
    distancia_desde_origen: float
) -> float:
    """
    Calcula el puntaje de recomendación de un destino.
    Mayor puntaje significa mejor recomendación.
    """

    puntaje = 0.0

    intereses_usuario = [
        interes.lower().strip()
        for interes in solicitud.intereses
    ]

    intereses_destino = [
        interes.lower().strip()
        for interes in destino["intereses"].split(",")
    ]

    coincidencias = set(intereses_usuario).intersection(set(intereses_destino))

    puntaje += len(coincidencias) * 25

    if not intereses_usuario:
        puntaje += 10

    if solicitud.presupuesto:
        if destino["costo_estimado"] <= solicitud.presupuesto:
            puntaje += 20
        else:
            puntaje -= 15

    if solicitud.distancia_maxima_km:
        if distancia_desde_origen <= solicitud.distancia_maxima_km:
            puntaje += 20
        else:
            puntaje -= 25

    if distancia_desde_origen <= 150:
        puntaje += 15
    elif distancia_desde_origen <= 300:
        puntaje += 8

    return round(puntaje, 2)


def recomendar_destinos(
    db: Session,
    solicitud: RecomendacionRequest,
    limite: int | None = None
) -> list[dict]:
    """
    Recomienda destinos turísticos con base en:
    - Intereses
    - Presupuesto
    - Distancia máxima
    - Cercanía al origen
    """

    destinos_bd = (
        db.query(Destino)
        .filter(Destino.activo == True)
        .all()
    )

    destinos_recomendados = []

    for destino_bd in destinos_bd:
        destino = convertir_destino_a_dict(destino_bd)

        distancia_desde_origen = haversine_distance(
            solicitud.latitud_origen,
            solicitud.longitud_origen,
            destino["latitud"],
            destino["longitud"]
        )

        if solicitud.distancia_maxima_km:
            if distancia_desde_origen > solicitud.distancia_maxima_km:
                continue

        puntaje = calcular_puntaje_destino(
            destino,
            solicitud,
            distancia_desde_origen
        )

        destino["puntaje_recomendacion"] = puntaje
        destino["distancia_desde_origen_km"] = distancia_desde_origen

        destinos_recomendados.append(destino)

    destinos_recomendados.sort(
        key=lambda destino: (
            destino["puntaje_recomendacion"],
            -destino["distancia_desde_origen_km"]
        ),
        reverse=True
    )

    if limite:
        return destinos_recomendados[:limite]

    return destinos_recomendados