from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.recomendacion_schema import RecomendacionRequest
from app.schemas.ruta_schema import RutaGeneradaResponse
from app.services.ruta_service import generar_ruta_optimizada


router = APIRouter()


@router.post("/generar", response_model=RutaGeneradaResponse)
def generar_ruta(
    solicitud: RecomendacionRequest,
    db: Session = Depends(get_db)
):
    """
    Genera una ruta turística optimizada con base en las preferencias del usuario.
    """

    return generar_ruta_optimizada(
        db=db,
        solicitud=solicitud
    )