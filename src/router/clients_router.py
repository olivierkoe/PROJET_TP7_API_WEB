from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import get_db
from models import Client
router_client = APIRouter()

# Modèles Pydantic pour validationclass ClientCreate(BaseModel):
class ClientCreate(BaseModel):
    genrecli: Optional[str] = None
    nomcli: str
    prenomcli: Optional[str] = None
    adresse1cli: Optional[str] = None
    adresse2cli: Optional[str] = None
    adresse3cli: Optional[str] = None
    villecli_id: Optional[int] = None
    telcli: Optional[str] = None
    emailcli: str
    portcli: Optional[str] = None
    newsletter: Optional[int] = None

class ClientUpdate(BaseModel):
    genrecli: Optional[str] = None
    nomcli: Optional[str] = None
    prenomcli: Optional[str] = None
    adresse1cli: Optional[str] = None
    adresse2cli: Optional[str] = None
    adresse3cli: Optional[str] = None
    villecli_id: Optional[int] = None
    telcli: Optional[str] = None
    emailcli: Optional[str] = None
    portcli: Optional[str] = None
    newsletter: Optional[int] = None

# Routes
@router_client.get("/clients", summary="Récupérer la liste des clients", description="Retourne une liste de tous les clients disponibles.")
async def get_clients(db: Session = Depends(get_db)):
    clients = db.query(Client).all()
    return clients

@router_client.post("/clients/")
async def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    # Vérifiez si un client avec le même email (emailcli) existe déjà
    existing_client = db.query(Client).filter(Client.emailcli == client.emailcli).first()  # Vérification avec emailcli
    
    if existing_client:
        raise HTTPException(status_code=400, detail="Un client avec cet email existe déjà")
    
    # Créez un nouveau client avec toutes les informations
    new_client = Client(
        genrecli=client.genrecli,
        nomcli=client.nomcli,
        prenomcli=client.prenomcli,
        adresse1cli=client.adresse1cli,
        adresse2cli=client.adresse2cli,
        adresse3cli=client.adresse3cli,
        villecli_id=client.villecli_id,
        telcli=client.telcli,
        emailcli=client.emailcli,
        portcli=client.portcli,
        newsletter=client.newsletter
    )
    
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    
    return new_client



# @router_client.put("/clients/{client_id}", summary="Mettre à jour un client", description="Met à jour les informations d'un client existant.")
# async def update_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)):
#     db_client = db.query(Client).filter(Client.id == client_id).first()
#     if not db_client:
#         raise HTTPException(status_code=404, detail="Client non trouvé")
#     if client.name:
#         db_client.name = client.name
#     if client.email:
#         db_client.email = client.email
#     db.commit()
#     db.refresh(db_client)
#     return {"message": "Client mis à jour avec succès", "client": db_client}

# @router_client.delete("/clients/{client_id}", summary="Supprimer un client", description="Supprime un client de la base de données.")
# async def delete_client(client_id: int, db: Session = Depends(get_db)):
#     db_client = db.query(Client).filter(Client.id == client_id).first()
#     if not db_client:
#         raise HTTPException(status_code=404, detail="Client non trouvé")
#     db.delete(db_client)
#     db.commit()
#     return {"message": f"Client avec ID {client_id} supprimé avec succès"}
