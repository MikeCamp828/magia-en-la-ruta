from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.routers import auth_router
from app.routers import destinos_router
from app.routers import recomendaciones_router
from app.routers import rutas_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API del sistema Magia en la Ruta para recomendación y optimización de rutas turísticas."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a la API de Magia en la Ruta",
        "estado": "funcionando",
        "documentacion": "/docs"
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        resultado = db.execute(text("SELECT COUNT(*) FROM destinos;")).scalar()

        return {
            "status": "ok",
            "database": "conectada",
            "destinos_registrados": resultado
        }

    except Exception as error:
        return {
            "status": "error",
            "database": "no conectada",
            "detalle": str(error)
        }


app.include_router(
    auth_router.router,
    prefix="/api/auth",
    tags=["Autenticación"]
)

app.include_router(
    destinos_router.router,
    prefix="/api/destinos",
    tags=["Destinos"]
)

app.include_router(
    recomendaciones_router.router,
    prefix="/api/recomendaciones",
    tags=["Recomendaciones"]
)

app.include_router(
    rutas_router.router,
    prefix="/api/rutas",
    tags=["Rutas"]
)