from pathlib import Path
import sys

from sqlalchemy.orm import Session

from app.schemas.recomendacion_schema import RecomendacionRequest
from app.services.recomendador_service import recomendar_destinos

# Permite importar el paquete optimizer desde la raíz del proyecto.
PROJECT_ROOT = Path(__file__).resolve().parents[3]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from optimizer.genetic_algorithm import optimizar_ruta_genetico
from optimizer.cost_calculator import calcular_costo_total, calcular_tiempo_total


def generar_ruta_optimizada(
    db: Session,
    solicitud: RecomendacionRequest
) -> dict:
    """
    Genera una ruta turística optimizada usando destinos recomendados
    y un algoritmo genético simple.
    """

    limite_candidatos = max(solicitud.cantidad_destinos * 4, 8)

    destinos_candidatos = recomendar_destinos(
        db=db,
        solicitud=solicitud,
        limite=limite_candidatos
    )

    if not destinos_candidatos:
        return {
            "origen": solicitud.origen,
            "tipo_ruta": solicitud.tipo_ruta,
            "distancia_total_km": 0.0,
            "tiempo_total_horas": 0.0,
            "costo_total_estimado": 0.0,
            "destinos": [],
            "mensaje": "No se encontraron destinos que coincidan con las preferencias indicadas."
        }

    origen = {
        "nombre": solicitud.origen,
        "latitud": solicitud.latitud_origen,
        "longitud": solicitud.longitud_origen
    }

    resultado_algoritmo = optimizar_ruta_genetico(
        origen=origen,
        destinos=destinos_candidatos,
        cantidad_destinos=solicitud.cantidad_destinos
    )

    ruta = resultado_algoritmo["ruta"]
    distancia_total = resultado_algoritmo["distancia_total_km"]

    costo_total = calcular_costo_total(
        distancia_total_km=distancia_total,
        destinos=ruta,
        tipo_ruta=solicitud.tipo_ruta
    )

    tiempo_total = calcular_tiempo_total(
        distancia_total_km=distancia_total,
        tipo_ruta=solicitud.tipo_ruta
    )

    destinos_respuesta = []

    for indice, destino in enumerate(ruta, start=1):
        destinos_respuesta.append({
            "orden_visita": indice,
            "id_destino": destino["id_destino"],
            "nombre": destino["nombre"],
            "estado": destino["estado"],
            "tipo": destino["tipo"],
            "descripcion": destino["descripcion"],
            "latitud": destino["latitud"],
            "longitud": destino["longitud"],
            "costo_estimado": destino["costo_estimado"],
            "tiempo_visita_horas": destino["tiempo_visita_horas"],
            "intereses": destino["intereses"],
            "imagen_url": destino["imagen_url"]
        })

    return {
        "origen": solicitud.origen,
        "tipo_ruta": solicitud.tipo_ruta,
        "distancia_total_km": distancia_total,
        "tiempo_total_horas": tiempo_total,
        "costo_total_estimado": costo_total,
        "destinos": destinos_respuesta,
        "mensaje": "Ruta generada correctamente con el algoritmo genético."
    }