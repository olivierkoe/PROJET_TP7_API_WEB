# routers/conditionnement.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.conditionnements_services import (
    fetch_all_conditionnements,
    fetch_conditionnement_by_id,
    add_conditionnement,
    modify_conditionnement,
    remove_conditionnement
)
from schemas.conditionnement import Conditionnement, ConditionnementCreate
from database import get_db

router_conditionnement = APIRouter()

# Route pour récupérer tous les conditionnements
@router_conditionnement.get("/", response_model=list[Conditionnement], tags=["Conditionnements"])
def get_conditionnements(db: Session = Depends(get_db)):
    return fetch_all_conditionnements(db)

# Route pour récupérer un conditionnement par ID
@router_conditionnement.get("/{idcondit}", response_model=Conditionnement, tags=["Conditionnements"])
def get_conditionnement(idcondit: int, db: Session = Depends(get_db)):
    conditionnement = fetch_conditionnement_by_id(db, idcondit)
    if not conditionnement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    return conditionnement

# Route pour créer un nouveau conditionnement
@router_conditionnement.post("/", response_model=Conditionnement, status_code=status.HTTP_201_CREATED, tags=["Conditionnements"])
def create_conditionnement(conditionnement_data: ConditionnementCreate, db: Session = Depends(get_db)):
    return add_conditionnement(db, conditionnement_data.dict())

# Route pour mettre à jour un conditionnement
@router_conditionnement.put("/{idcondit}", response_model=Conditionnement, tags=["Conditionnements"])
def update_conditionnement(idcondit: int, updated_data: dict, db: Session = Depends(get_db)):
    conditionnement = modify_conditionnement(db, idcondit, updated_data)
    if not conditionnement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    return conditionnement

# Route pour supprimer un conditionnement
@router_conditionnement.delete("/{idcondit}", status_code=status.HTTP_204_NO_CONTENT, tags=["Conditionnements"])
def delete_conditionnement(idcondit: int, db: Session = Depends(get_db)):
    conditionnement = remove_conditionnement(db, idcondit)
    if not conditionnement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
