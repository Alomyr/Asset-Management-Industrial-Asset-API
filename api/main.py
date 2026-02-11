from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

# define rotas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Gestão de Ativos Industriais")


@app.post("/assets/", response_model=schemas.AssetResponse)
def create_asset(asset: schemas.AssetBase, db: Session = Depends(get_db)):
    return crud.create_asset(db=db, asset=asset)


@app.get("/assets/", response_model=list[schemas.AssetResponse])
def read_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_assets(db, skip=skip, limit=limit)


@app.post("/user/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/user/", response_model=schemas.UserResponse)
def read_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/")
def home():
    return {"status": "API Online", "projeto": "Gestão de Ativos + AR"}


@app.get("/health")
def check_health():
    return {"status": "Healthy", "database": "Connected"}


models.Base.metadata.create_all(bind=engine)
