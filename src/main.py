
from fastapi import FastAPI
from router.clients_router import router_client
from router.departements_router import router_departement
from router.conditionnements_router import router_conditionnement
from router.commandes_router import router_commande
from router.communes_router import router_commune
from database import engine
from models import Base

app = FastAPI()

app.include_router(router_client, prefix="/clients", tags=["Clients"])
app.include_router(router_departement, prefix="/departements", tags=["Départements"])
app.include_router(router_conditionnement, prefix="/conditionnements", tags=["Conditionnements"])
app.include_router(router_commune, prefix="/communes", tags=["Communes"])
app.include_router(router_commande, prefix="/commandes", tags=["Commandes"])


# importer engine(database.py) et Base(models.py)
Base.metadata.create_all(engine)


