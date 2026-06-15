from typing import List, Optional

from pydantic import BaseModel


class DestinoRutaResponse(BaseModel):
    orden_visita: int
    id_destino: int
    nombre: str
    estado: str
    tipo: str
    descripcion: str
    latitud: float
    longitud: float
    costo_estimado: float
    tiempo_visita_horas: float
    intereses: str
    imagen_url: Optional[str] = None


class RutaGeneradaResponse(BaseModel):
    origen: str
    tipo_ruta: str
    distancia_total_km: float
    tiempo_total_horas: float
    costo_total_estimado: float
    destinos: List[DestinoRutaResponse]
    mensaje: str