from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.recomendacion_schema import (
    RecomendacionRequest,
    DestinoRecomendadoResponse
)
from app.services.recomendador_service import recomendar_destinos


router = APIRouter()


@router.post("/", response_model=List[DestinoRecomendadoResponse])
def obtener_recomendaciones(
    solicitud: RecomendacionRequest,
    db: Session = Depends(get_db)
):
    """
    Recibe las preferencias del usuario y devuelve destinos recomendados.
    """

    destinos = recomendar_destinos(
        db=db,
        solicitud=solicitud,
        limite=10
    )

    return destinos