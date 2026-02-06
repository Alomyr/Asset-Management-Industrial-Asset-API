from sqlalchemy.orm import Session
import models, schemas  # Sem o ponto antes do models/schemas


def create_asset(db: Session, asset: schemas.AssetCreate):
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
