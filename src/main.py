
from fastapi import FastAPI
from router.clients_router import router_client
from database import engine
from models import Base

app = FastAPI()
app.include_router(router_client)

# importer engine(database.py) et Base(models.py)
Base.metadata.create_all(engine)

@app.get("/")
def toto():
    return {"message": "Hello World"}

