from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.commandes_services import (
    create_commande, 
    get_all_commandes, 
    get_commande_by_id, 
    update_commande, 
    delete_commande
)
from schemas.commande import CommandeCreate, CommandeResponse
from database import get_db

# Définir le routeur pour les commandes
router_commande = APIRouter()

# Route pour créer une nouvelle commande
@router_commande.post("/commandes/", response_model=CommandeResponse, status_code=status.HTTP_201_CREATED)
def create_new_commande(commande_data: CommandeCreate, db: Session = Depends(get_db)):
    return create_commande(db=db, commande_data=commande_data)

# Route pour récupérer toutes les commandes
@router_commande.get("/commandes/", response_model=list[CommandeResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_commandes(db)

# Route pour récupérer une commande par ID
@router_commande.get("/commandes/{codcde}", response_model=CommandeResponse)
def get_by_id(codcde: int, db: Session = Depends(get_db)):
    commande = get_commande_by_id(db=db, codcde=codcde)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    return commande

# Route pour mettre à jour une commande par ID
@router_commande.put("/commandes/{codcde}", response_model=CommandeResponse)
def update_commande_by_id(codcde: int, updated_data: CommandeCreate, db: Session = Depends(get_db)):
    commande = update_commande(db=db, codcde=codcde, updated_data=updated_data)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    return commande

# Route pour supprimer une commande par ID
@router_commande.delete("/commandes/{codcde}", status_code=status.HTTP_204_NO_CONTENT)
def delete_commande_by_id(codcde: int, db: Session = Depends(get_db)):
    commande = get_commande_by_id(db=db, codcde=codcde)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    
    delete_commande(db=db, codcde=codcde)
    return {"message": "Commande deleted successfully"}
