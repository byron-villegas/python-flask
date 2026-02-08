from pydantic import BaseModel, Field, field_validator
from typing import Optional


class ProductDto(BaseModel):
    """
    DTO para representar un producto completo
    """
    sku: int = Field(..., description="SKU único del producto", example=12345, gt=0)
    name: str = Field(..., description="Nombre del producto", example="Laptop Dell XPS 15", min_length=1, max_length=200)
    price: float = Field(..., description="Precio del producto", example=1299.99, gt=0)
    description: Optional[str] = Field(None, description="Descripción detallada del producto", example="Laptop Dell XPS 15 con procesador Intel Core i7")
    
    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        """Valida que el nombre no sea una cadena vacía"""
        if not v or v.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")
        return v.strip()
    
    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        """Valida que el precio sea positivo"""
        if v <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        return round(v, 2)
    
    class Config:
        """Configuración del modelo Pydantic"""
        json_schema_extra = {
            "example": {
                "sku": 12345,
                "name": "Laptop Dell XPS 15",
                "price": 1299.99,
                "description": "Laptop Dell XPS 15 con procesador Intel Core i7, 16GB RAM, 512GB SSD"
            }
        }


class CreateProductDto(BaseModel):
    """
    DTO para crear un nuevo producto (sin validar que el SKU no exista aún)
    """
    sku: int = Field(..., description="SKU único del producto", example=12345, gt=0)
    name: str = Field(..., description="Nombre del producto", example="Laptop Dell XPS 15", min_length=1, max_length=200)
    price: float = Field(..., description="Precio del producto", example=1299.99, gt=0)
    description: Optional[str] = Field(None, description="Descripción detallada del producto", example="Laptop Dell XPS 15 con procesador Intel Core i7")
    
    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        """Valida que el nombre no sea una cadena vacía"""
        if not v or v.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")
        return v.strip()
    
    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        """Valida que el precio sea positivo"""
        if v <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        return round(v, 2)
    
    class Config:
        """Configuración del modelo Pydantic"""
        json_schema_extra = {
            "example": {
                "sku": 12345,
                "name": "Laptop Dell XPS 15",
                "price": 1299.99,
                "description": "Laptop Dell XPS 15 con procesador Intel Core i7, 16GB RAM, 512GB SSD"
            }
        }
    
    def to_dict(self) -> dict:
        """
        Convierte el DTO a un diccionario
        
        Returns:
            dict: Representación del DTO como diccionario
        """
        return self.model_dump(exclude_none=True)
