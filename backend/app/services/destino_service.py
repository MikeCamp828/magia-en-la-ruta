from sqlalchemy.orm import Session

from app.models.destino_model import Destino


def obtener_destinos(
    db: Session,
    q: str | None = None,
    estado: str | None = None,
    tipo: str | None = None,
    interes: str | None = None
):
    """
    Obtiene destinos turísticos desde la base de datos.
    Permite filtrar por búsqueda, estado, tipo e interés.
    """

    consulta = db.query(Destino).filter(Destino.activo == True)

    if q:
        consulta = consulta.filter(Destino.nombre.ilike(f"%{q}%"))

    if estado:
        consulta = consulta.filter(Destino.estado.ilike(f"%{estado}%"))

    if tipo:
        consulta = consulta.filter(Destino.tipo.ilike(f"%{tipo}%"))

    if interes:
        consulta = consulta.filter(Destino.intereses.ilike(f"%{interes}%"))

    return consulta.order_by(Destino.nombre.asc()).all()


def obtener_destino_por_id(db: Session, id_destino: int):
    """
    Obtiene un destino específico por su ID.
    """

    return (
        db.query(Destino)
        .filter(Destino.id_destino == id_destino)
        .filter(Destino.activo == True)
        .first()
    )