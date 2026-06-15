from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, Text
from sqlalchemy.sql import func

from app.db.database import Base


class Destino(Base):
    __tablename__ = "destinos"

    id_destino = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    estado = Column(String(100), nullable=False)
    tipo = Column(String(80), nullable=False)
    descripcion = Column(Text, nullable=False)

    latitud = Column(Numeric(10, 7), nullable=False)
    longitud = Column(Numeric(10, 7), nullable=False)

    costo_estimado = Column(Numeric(10, 2), default=0)
    tiempo_visita_horas = Column(Numeric(5, 2), default=2)

    intereses = Column(Text, nullable=False)
    imagen_url = Column(Text)

    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, server_default=func.now())