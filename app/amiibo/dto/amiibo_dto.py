from pydantic import BaseModel, Field
from typing import Optional


class AmiiboDto(BaseModel):
    """
    DTO para representar la información de un Amiibo
    """
    name: str = Field(..., description="Nombre del Amiibo", example="Link")
    character: str = Field(..., description="Personaje del Amiibo", example="Link")
    image: str = Field(..., description="URL de la imagen del Amiibo", example="https://raw.githubusercontent.com/N3evin/AmiiboAPI/master/images/icon_00000000-00000002.png")
    amiiboSeries: str = Field(..., description="Serie del Amiibo", example="The Legend of Zelda")
    gameSeries: str = Field(..., description="Serie del juego", example="The Legend of Zelda")
    
    class Config:
        """Configuración del modelo Pydantic"""
        json_schema_extra = {
            "example": {
                "name": "Link",
                "character": "Link",
                "image": "https://raw.githubusercontent.com/N3evin/AmiiboAPI/master/images/icon_00000000-00000002.png",
                "amiiboSeries": "The Legend of Zelda",
                "gameSeries": "The Legend of Zelda"
            }
        }
    
    @classmethod
    def from_json(cls, amiibo: dict) -> "AmiiboDto":
        """
        Crea una instancia de AmiiboDto desde un diccionario JSON
        
        Args:
            amiibo: Diccionario con los datos del amiibo
            
        Returns:
            AmiiboDto: Instancia del DTO con los datos del amiibo
        """
        return cls(
            name=amiibo.get("name", ""),
            character=amiibo.get("character", ""),
            image=amiibo.get("image", ""),
            amiiboSeries=amiibo.get("amiiboSeries", ""),
            gameSeries=amiibo.get("gameSeries", "")
        )
    
    def to_dict(self) -> dict:
        """
        Convierte el DTO a un diccionario
        
        Returns:
            dict: Representación del DTO como diccionario
        """
        return self.model_dump()