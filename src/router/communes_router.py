# routers/commune.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.communes_services import (
    fetch_all_communes,
    fetch_commune_by_id,
    add_commune,
    modify_commune,
    remove_commune
)
from schemas.commune import Commune, CommuneCreate
from database import get_db

router_commune = APIRouter()

# Route pour récupérer toutes les communes
@router_commune.get("/", response_model=list[Commune], tags=["Communes"])
def get_communes(db: Session = Depends(get_db)):
    return fetch_all_communes(db)

# Route pour récupérer une commune par ID
@router_commune.get("/{id}", response_model=Commune, tags=["Communes"])
def get_commune(id: int, db: Session = Depends(get_db)):
    commune = fetch_commune_by_id(db, id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    return commune

# Route pour créer une nouvelle commune
@router_commune.post("/", response_model=Commune, status_code=status.HTTP_201_CREATED, tags=["Communes"])
def create_commune(commune_data: CommuneCreate, db: Session = Depends(get_db)):
    return add_commune(db, commune_data.dict())

# Route pour mettre à jour une commune
@router_commune.put("/{id}", response_model=Commune, tags=["Communes"])
def update_commune(id: int, updated_data: dict, db: Session = Depends(get_db)):
    commune = modify_commune(db, id, updated_data)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    return commune

# Route pour supprimer une commune
@router_commune.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Communes"])
def delete_commune(id: int, db: Session = Depends(get_db)):
    commune = remove_commune(db, id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
