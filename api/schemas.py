from pydantic import BaseModel
from typing import Optional, List


# O que o usuário envia ao criar um Ativo
class AssetCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True


# O que a API devolve (incluindo o ID gerado)
class AssetResponse(AssetCreate):
    id: int
