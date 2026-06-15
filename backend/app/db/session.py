from app.db.database import SessionLocal


def get_db():
    """
    Crea una sesión de base de datos para cada petición.
    Al terminar la petición, la sesión se cierra automáticamente.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()