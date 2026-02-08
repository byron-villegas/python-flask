"""
Esquemas de Swagger generados automáticamente desde los DTOs de Pydantic
"""
from app.auth.dto import LoginDto, UserDto, TokenResponseDto
from app.product.dto import ProductDto, CreateProductDto
from app.amiibo.dto import AmiiboDto


def get_swagger_definitions():
    """
    Genera las definiciones de Swagger desde los modelos de Pydantic
    
    Returns:
        dict: Diccionario con todas las definiciones de esquemas
    """
    return {
        "LoginDto": LoginDto.model_json_schema(),
        "UserDto": UserDto.model_json_schema(),
        "TokenResponseDto": TokenResponseDto.model_json_schema(),
        "ProductDto": ProductDto.model_json_schema(),
        "CreateProductDto": CreateProductDto.model_json_schema(),
        "AmiiboDto": AmiiboDto.model_json_schema(),
        "ErrorResponse": {
            "type": "object",
            "properties": {
                "statusCode": {
                    "type": "integer",
                    "description": "Código de estado HTTP",
                    "example": 400
                },
                "message": {
                    "type": "string",
                    "description": "Mensaje de error",
                    "example": "Datos inválidos"
                },
                "errors": {
                    "type": "array",
                    "description": "Lista de errores de validación",
                    "items": {
                        "type": "object",
                        "properties": {
                            "loc": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Ubicación del error"
                            },
                            "msg": {
                                "type": "string",
                                "description": "Mensaje del error"
                            },
                            "type": {
                                "type": "string",
                                "description": "Tipo de error"
                            }
                        }
                    }
                }
            }
        }
    }
