from fastapi import APIRouter, HTTPException, Depends, status
from models import Client
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from services.clients_services import get_all, get_by_id, create_client, update_client, delete_client
from schemas.client import ClientCreate, ClientResponse

router_client = APIRouter()

@router_client.get("/", response_model=List[ClientResponse], tags=["Clients"])
def get_clients(db: Session = Depends(get_db)):
    """Fetch all clients."""
    try:
        clients = get_all(db)
        return db.query(Client).all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching clients: {str(e)}"
        )

@router_client.get("/{id}", response_model=ClientResponse, tags=["Clients"])
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    """Fetch a single client by ID."""
    client = get_by_id(db, id)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client with ID {id} not found."
        )
    return client

@router_client.post("/", response_model=ClientResponse, status_code=status.HTTP_201_CREATED, tags=["Clients"])
def add_client(client_data: ClientCreate, db: Session = Depends(get_db)):
    """Create a new client."""
    try:
        new_client = create_client(db, client_data.model_dump())
        return new_client
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An error occurred while creating the client: {str(e)}"
        )

@router_client.put("/{id}", response_model=ClientResponse, status_code=status.HTTP_200_OK, tags=["Clients"])
def update_client_data(id: int, updated_data: ClientCreate, db: Session = Depends(get_db)):
    """
    Update the data of an existing client.
    :param id: Client ID
    :param updated_data: Updated data for the client
    :param db: Database session
    :return: Updated client object
    """
    try:
        updated_client = update_client(db, id, updated_data.dict())
        if not updated_client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
        return updated_client
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the client: {str(e)}"
        )

@router_client.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Clients"])
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
