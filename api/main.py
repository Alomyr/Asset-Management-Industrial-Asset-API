from fastapi import FastAPI
import models
from database import engine

app = FastAPI(title="API de Gestão de Ativos Industriais")


@app.get("/")
def home():
    return {"status": "API Online", "projeto": "Gestão de Ativos + AR"}


@app.get("/health")
def check_health():
    return {"status": "Healthy", "database": "Connected"}


models.Base.metadata.create_all(bind=engine)
