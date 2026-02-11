from unittest import skip
from sqlalchemy.orm import Session
import models, schemas


# funcoes de salvar, consultar e etc
def create_asset(db: Session, asset: schemas.AssetBase):
    db_asset = models.Asset(
        name=asset.name,
        description=asset.description,
        category=asset.category,
        parent_id=asset.parent_id,
    )
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset


def get_assets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Asset).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password,
        parent_is=user.parent_id,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).offset(models.User.id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
