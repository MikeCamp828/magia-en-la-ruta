from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings


pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


def encriptar_password(password: str) -> str:
    """
    Encripta una contraseña antes de guardarla en la base de datos.
    Se usa pbkdf2_sha256 para evitar problemas de compatibilidad con bcrypt.
    """
    return pwd_context.hash(password)


def verificar_password(password_plano: str, password_hash: str) -> bool:
    """
    Verifica si una contraseña escrita coincide con su versión encriptada.
    """
    return pwd_context.verify(password_plano, password_hash)


def crear_token_acceso(data: dict) -> str:
    """
    Crea un token JWT para mantener la sesión del usuario.
    """
    datos_a_codificar = data.copy()

    expiracion = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    datos_a_codificar.update({"exp": expiracion})

    token = jwt.encode(
        datos_a_codificar,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token


def obtener_correo_desde_token(token: str) -> str | None:
    """
    Decodifica el token y obtiene el correo del usuario.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        correo = payload.get("sub")

        return correo

    except JWTError:
        return None