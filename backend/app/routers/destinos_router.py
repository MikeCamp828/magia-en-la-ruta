from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.destino_schema import DestinoResponse
from app.services.destino_service import obtener_destino_por_id, obtener_destinos


router = APIRouter()


@router.get("/", response_model=List[DestinoResponse])
def listar_destinos(
    q: Optional[str] = Query(default=None, description="Buscar por nombre del destino"),
    estado: Optional[str] = Query(default=None, description="Filtrar por estado"),
    tipo: Optional[str] = Query(default=None, description="Filtrar por tipo de destino"),
    interes: Optional[str] = Query(default=None, description="Filtrar por interés"),
    db: Session = Depends(get_db)
):
    """
    Lista destinos turísticos registrados en la base de datos.
    """

    destinos = obtener_destinos(
        db=db,
        q=q,
        estado=estado,
        tipo=tipo,
        interes=interes
    )

    return destinos


@router.get("/{id_destino}", response_model=DestinoResponse)
def detalle_destino(
    id_destino: int,
    db: Session = Depends(get_db)
):
    """
    Devuelve la información de un destino específico.
    """

    destino = obtener_destino_por_id(db, id_destino)

    if not destino:
        raise HTTPException(
            status_code=404,
            detail="Destino no encontrado"
        )

    return destino