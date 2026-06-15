from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.usuario_model import Usuario
from app.routers.auth_router import obtener_usuario_actual
from app.schemas.opinion_schema import (
    OpinionCreate,
    OpinionResponse,
    OpinionResumenResponse
)
from app.services.opinion_service import (
    crear_opinion,
    obtener_opiniones_por_destino,
    obtener_resumen_opiniones_destino
)


router = APIRouter()


@router.post("/", response_model=OpinionResponse)
def publicar_opinion(
    datos: OpinionCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    """
    Publica una opinión de un destino.
    Requiere que el usuario esté autenticado.
    """

    opinion = crear_opinion(
        db=db,
        id_usuario=usuario_actual.id_usuario,
        datos=datos
    )

    if not opinion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Destino no encontrado"
        )

    return {
        "id_opinion": opinion.id_opinion,
        "id_usuario": usuario_actual.id_usuario,
        "nombre_usuario": usuario_actual.nombre,
        "id_destino": opinion.id_destino,
        "calificacion": opinion.calificacion,
        "comentario": opinion.comentario,
        "fecha_creacion": opinion.fecha_creacion
    }


@router.get("/destino/{id_destino}", response_model=List[OpinionResponse])
def listar_opiniones_destino(
    id_destino: int,
    db: Session = Depends(get_db)
):
    """
    Lista las opiniones publicadas para un destino.
    """

    return obtener_opiniones_por_destino(
        db=db,
        id_destino=id_destino
    )


@router.get("/destino/{id_destino}/resumen", response_model=OpinionResumenResponse)
def resumen_opiniones_destino(
    id_destino: int,
    db: Session = Depends(get_db)
):
    """
    Devuelve el promedio de calificación y número de opiniones de un destino.
    """

    return obtener_resumen_opiniones_destino(
        db=db,
        id_destino=id_destino
    )