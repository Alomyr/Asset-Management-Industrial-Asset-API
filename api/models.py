from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


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
