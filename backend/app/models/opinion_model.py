from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.sql import func

from app.db.database import Base


class Opinion(Base):
    __tablename__ = "opiniones"

    id_opinion = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), nullable=False)
    id_destino = Column(Integer, ForeignKey("destinos.id_destino", ondelete="CASCADE"), nullable=False)
    calificacion = Column(Integer, nullable=False)
    comentario = Column(Text, nullable=False)
    fecha_creacion = Column(DateTime, server_default=func.now())


class OpinionFoto(Base):
    __tablename__ = "opinion_fotos"

    id_foto = Column(Integer, primary_key=True, index=True)
    id_opinion = Column(Integer, ForeignKey("opiniones.id_opinion", ondelete="CASCADE"), nullable=False)
    ruta_foto = Column(Text, nullable=False)
    fecha_subida = Column(DateTime, server_default=func.now())