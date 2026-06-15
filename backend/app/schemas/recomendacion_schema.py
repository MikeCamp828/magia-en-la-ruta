from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class RecomendacionRequest(BaseModel):
    origen: str = Field(default="Ciudad de México")
    latitud_origen: float = Field(default=19.432608)
    longitud_origen: float = Field(default=-99.133209)

    presupuesto: Optional[float] = None
    distancia_maxima_km: Optional[float] = None

    cantidad_destinos: int = Field(default=3, ge=1, le=8)
    tipo_ruta: str = Field(default="libre")

    intereses: List[str] = Field(default_factory=list)


class DestinoRecomendadoResponse(BaseModel):
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

    puntaje_recomendacion: float
    distancia_desde_origen_km: float

    model_config = ConfigDict(from_attributes=True)