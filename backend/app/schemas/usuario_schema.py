from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UsuarioRegistro(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    correo: EmailStr
    password: str = Field(min_length=6)


class UsuarioLogin(BaseModel):
    correo: EmailStr
    password: str


class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre: str
    correo: str

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: UsuarioResponse