from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.destino_model import Destino
from app.models.opinion_model import Opinion
from app.models.usuario_model import Usuario
from app.schemas.opinion_schema import OpinionCreate


def crear_opinion(
    db: Session,
    id_usuario: int,
    datos: OpinionCreate
):
    """
    Crea una opinión para un destino turístico.
    """

    destino = (
        db.query(Destino)
        .filter(Destino.id_destino == datos.id_destino)
        .filter(Destino.activo == True)
        .first()
    )

    if not destino:
        return None

    nueva_opinion = Opinion(
        id_usuario=id_usuario,
        id_destino=datos.id_destino,
        calificacion=datos.calificacion,
        comentario=datos.comentario
    )

    db.add(nueva_opinion)
    db.commit()
    db.refresh(nueva_opinion)

    return nueva_opinion


def obtener_opiniones_por_destino(
    db: Session,
    id_destino: int
):
    """
    Obtiene todas las opiniones de un destino junto con el nombre del usuario.
    """

    resultados = (
        db.query(
            Opinion.id_opinion,
            Opinion.id_usuario,
            Usuario.nombre.label("nombre_usuario"),
            Opinion.id_destino,
            Opinion.calificacion,
            Opinion.comentario,
            Opinion.fecha_creacion
        )
        .join(Usuario, Usuario.id_usuario == Opinion.id_usuario)
        .filter(Opinion.id_destino == id_destino)
        .order_by(Opinion.fecha_creacion.desc())
        .all()
    )

    opiniones = []

    for item in resultados:
        opiniones.append({
            "id_opinion": item.id_opinion,
            "id_usuario": item.id_usuario,
            "nombre_usuario": item.nombre_usuario,
            "id_destino": item.id_destino,
            "calificacion": item.calificacion,
            "comentario": item.comentario,
            "fecha_creacion": item.fecha_creacion
        })

    return opiniones


def obtener_resumen_opiniones_destino(
    db: Session,
    id_destino: int
):
    """
    Obtiene el promedio de calificación y total de opiniones de un destino.
    """

    resultado = (
        db.query(
            func.count(Opinion.id_opinion).label("total"),
            func.coalesce(func.avg(Opinion.calificacion), 0).label("promedio")
        )
        .filter(Opinion.id_destino == id_destino)
        .first()
    )

    return {
        "id_destino": id_destino,
        "total_opiniones": int(resultado.total),
        "promedio_calificacion": round(float(resultado.promedio), 2)
    }