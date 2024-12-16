from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from models import Client
from database import get_db
from services.clients_services import get_all, get_by_id, create_client, update_client, delete_client

router_client = APIRouter()

# Pydantic Model for Client
class ClientCreate(BaseModel):
    nomcli: str
    emailcli: str

    class Config:
        orm_mode = True

@router_client.get("/", response_model=List[ClientCreate])
def get_clients(db: Session = Depends(get_db)):
    """Fetch all clients."""
    try:
        return get_all(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching clients: {str(e)}"
        )

@router_client.get("/{id}", response_model=ClientCreate)
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    """Fetch a single client by ID."""
    client = get_by_id(db, id)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client with ID {id} not found."
        )
    return client

@router_client.post("/", response_model=ClientCreate, status_code=status.HTTP_201_CREATED)
def add_client(client_data: ClientCreate, db: Session = Depends(get_db)):
    """Create a new client."""
    try:
        return create_client(db, client_data.dict())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An error occurred while creating the client: {str(e)}"
        )

@router_client.put("/{codcli}", status_code=status.HTTP_200_OK)
def update_client_data(codcli: int, updated_data: dict, db: Session = Depends(get_db)):
    """
    Met à jour les données d'un client.
    :param codcli: Identifiant du client
    :param updated_data: Données mises à jour
    :param db: Session de base de données
    :return: Client mis à jour
    """
    try:
        return update_client(db, codcli, updated_data)
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router_client.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_client(id: int, db: Session = Depends(get_db)):
    """Delete a client by ID."""
    client = get_by_id(db, id)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client with ID {id} not found."
        )
    try:
        delete_client(db, id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the client: {str(e)}"
        )
