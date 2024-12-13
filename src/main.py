# importer fastapi
from fastapi import FastAPI
from src.database import engine
from src.models import Base

# definir les routes
app = FastAPI()

# importer engine(database.py) et Base(models.py)
Base.metadata.create_all(engine)


@app.get("/")
def toto():
    return {"message": "Hello World"}