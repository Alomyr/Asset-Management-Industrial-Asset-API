from pydoc import describe
from unicodedata import category
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


# traduz do py para o banco de dados
class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)  # Ex: Sensor, Motor, Galpão

    # --- ESTRUTURA DE NÓS (TREE) ---
    # Este campo aponta para o ID de outro ativo (o "Pai")
    parent_id = Column(Integer, ForeignKey("assets.id"), nullable=True)

    # Relacionamento para acessar o pai
    parent = relationship("Asset", remote_side=[id], backref="children")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    parent_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    parent = relationship("User", remote_side=[id], backref="subordinates")
