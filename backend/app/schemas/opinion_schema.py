from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class OpinionCreate(BaseModel):
    id_destino: int
    calificacion: int = Field(ge=1, le=5)
    comentario: str = Field(min_length=3, max_length=1000)


class OpinionResponse(BaseModel):
    id_opinion: int
    id_usuario: int
    nombre_usuario: str
    id_destino: int
    calificacion: int
    comentario: str
    fecha_creacion: datetime

    model_config = ConfigDict(from_attributes=True)


class OpinionResumenResponse(BaseModel):
    id_destino: int
    total_opiniones: int
    promedio_calificacion: float