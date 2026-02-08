from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional


class LoginDto(BaseModel):
    """
    DTO para autenticación de usuario
    """
    username: str = Field(..., description="Nombre de usuario", example="admin", min_length=3, max_length=50)
    password: str = Field(..., description="Contraseña del usuario", example="password123", min_length=6)
    
    @field_validator('username')
    @classmethod
    def username_must_not_be_empty(cls, v: str) -> str:
        """Valida que el username no sea una cadena vacía"""
        if not v or v.strip() == "":
            raise ValueError("El nombre de usuario no puede estar vacío")
        return v.strip()
    
    @field_validator('password')
    @classmethod
    def password_must_not_be_empty(cls, v: str) -> str:
        """Valida que la contraseña no sea una cadena vacía"""
        if not v or v.strip() == "":
            raise ValueError("La contraseña no puede estar vacía")
        return v
    
    class Config:
        """Configuración del modelo Pydantic"""
        json_schema_extra = {
            "example": {
                "username": "admin",
                "password": "password123"
            }
        }


class UserDto(BaseModel):
    """
    DTO para representar un usuario del sistema
    """
    username: str = Field(..., description="Nombre de usuario", example="admin")
    email: Optional[str] = Field(None, description="Correo electrónico del usuario", example="admin@example.com")
    full_name: Optional[str] = Field(None, description="Nombre completo del usuario", example="Admin User")
    is_active: bool = Field(True, description="Indicador de si el usuario está activo", example=True)
    
    class Config:
        """Configuración del modelo Pydantic"""
        json_schema_extra = {
            "example": {
                "username": "admin",
                "email": "admin@example.com",
                "full_name": "Admin User",
                "is_active": True
            }
        }
    
    def to_dict(self) -> dict:
        """
        Convierte el DTO a un diccionario
        
        Returns:
            dict: Representación del DTO como diccionario
        """
        return self.model_dump(exclude_none=True)


class TokenResponseDto(BaseModel):
    """
    DTO para la respuesta de autenticación con token JWT
    """
    access_token: str = Field(..., description="Token JWT de acceso", example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
    token_type: str = Field(default="Bearer", description="Tipo de token", example="Bearer")
    expires_in: int = Field(..., description="Tiempo de expiración del token en segundos", example=3600)
    
    class Config:
        """Configuración del modelo Pydantic"""
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                "token_type": "Bearer",
                "expires_in": 3600
            }
        }
