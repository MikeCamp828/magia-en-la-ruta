from typing import Optional
from pydantic import BaseModel, ConfigDict


class DestinoResponse(BaseModel):
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
    activo: bool

    model_config = ConfigDict(from_attributes=True)