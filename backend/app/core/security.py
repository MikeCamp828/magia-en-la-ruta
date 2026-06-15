from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encriptar_password(password: str) -> str:
    """
    Encripta una contraseña antes de guardarla en la base de datos.
    """
    return pwd_context.hash(password)


def verificar_password(password_plano: str, password_hash: str) -> bool:
    """
    Verifica si una contraseña escrita coincide con su versión encriptada.
    """
    return pwd_context.verify(password_plano, password_hash)