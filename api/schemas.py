from pydantic import BaseModel
from typing import Optional, List


# regras
# O que o usuário envia ao criar um Ativo
class AssetBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True


# O que a API devolve (incluindo o ID gerado)
class AssetResponse(AssetBase):
    id: int

    class confif:
        from_attributes = True


class AssetCreate(AssetBase):
    pass


# User
class UserBase(BaseModel):
    name: str
    email: str
    parent_id: Optional[int] = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
