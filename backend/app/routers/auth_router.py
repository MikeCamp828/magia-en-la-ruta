from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    crear_token_acceso,
    encriptar_password,
    obtener_correo_desde_token,
    verificar_password
)
from app.db.session import get_db
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import (
    TokenResponse,
    UsuarioLogin,
    UsuarioRegistro,
    UsuarioResponse
)


router = APIRouter()


def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()


def obtener_usuario_actual(
    authorization: str | None = Header(default=None),
    db: Session = Depends(get_db)
):
    """
    Lee el token enviado en el header Authorization.
    Formato esperado:
    Bearer token_aqui
    """

    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se envió token de autenticación"
        )

    partes = authorization.split()

    if len(partes) != 2 or partes[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de token inválido"
        )

    token = partes[1]
    correo = obtener_correo_desde_token(token)

    if not correo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )

    usuario = obtener_usuario_por_correo(db, correo)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )

    return usuario


@router.post("/registro", response_model=TokenResponse)
def registrar_usuario(
    datos: UsuarioRegistro,
    db: Session = Depends(get_db)
):
    """
    Registra un nuevo usuario y devuelve un token de sesión.
    """

    usuario_existente = obtener_usuario_por_correo(db, datos.correo)

    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una cuenta con ese correo"
        )

    nuevo_usuario = Usuario(
        nombre=datos.nombre,
        correo=datos.correo,
        password_hash=encriptar_password(datos.password)
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    token = crear_token_acceso({
        "sub": nuevo_usuario.correo,
        "id_usuario": nuevo_usuario.id_usuario
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "usuario": nuevo_usuario
    }


@router.post("/login", response_model=TokenResponse)
def iniciar_sesion(
    datos: UsuarioLogin,
    db: Session = Depends(get_db)
):
    """
    Inicia sesión con correo y contraseña.
    """

    usuario = obtener_usuario_por_correo(db, datos.correo)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos"
        )

    password_correcto = verificar_password(
        datos.password,
        usuario.password_hash
    )

    if not password_correcto:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos"
        )

    token = crear_token_acceso({
        "sub": usuario.correo,
        "id_usuario": usuario.id_usuario
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "usuario": usuario
    }


@router.get("/me", response_model=UsuarioResponse)
def obtener_mi_usuario(
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    """
    Devuelve los datos del usuario autenticado.
    """

    return usuario_actual