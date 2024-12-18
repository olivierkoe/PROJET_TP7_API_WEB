from fastapi import APIRouter, HTTPException, Depends, status  # Importation de FastAPI et des exceptions HTTP
from src.models import Client  # Importation du modèle Client pour interagir avec la base de données
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données via SQLAlchemy
from typing import List  # Pour spécifier que nous retournons une liste d'objets dans les réponses
from src.database import get_db  # Importation de la fonction pour récupérer une session de base de données
from src.services.clients_services import get_all, get_by_id, create_client, update_client, delete_client  # Importation des services
from src.schemas.client import ClientCreate, ClientResponse  # Importation des schémas de données pour la validation des entrées et sorties

router_client = APIRouter()  # Création d'un routeur pour les routes liées aux clients


@router_client.get("/", response_model=List[ClientResponse], tags=["Clients"])
def get_clients(db: Session = Depends(get_db)):
    """
    Récupère tous les clients depuis la base de données.
    :param db: Session de base de données
    :return: Liste de clients
    """
    try:
        clients = get_all(db)  # Récupère tous les clients via la fonction service
        return clients  # Retourne les clients récupérés
    except Exception as e:
        # Si une erreur se produit lors de la récupération des clients, renvoie une exception HTTP avec un message d'erreur
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching clients: {str(e)}"
        )


@router_client.get("/{id}", response_model=ClientResponse, tags=["Clients"])
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    """
    Récupère un client spécifique en fonction de son ID.
    :param id: ID du client
    :param db: Session de base de données
    :return: Le client correspondant à l'ID
    """
    client = get_by_id(db, id)  # Récupère le client via la fonction service
    if not client:
        # Si le client n'est pas trouvé, renvoie une erreur HTTP 404 avec un message
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client with ID {id} not found."
        )
    return client  # Retourne le client trouvé


@router_client.post("/", response_model=ClientResponse, status_code=status.HTTP_201_CREATED, tags=["Clients"])
def add_client(client_data: ClientCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau client dans la base de données.
    :param client_data: Données du client à créer
    :param db: Session de base de données
    :return: Le client créé
    """
    try:
        # Appelle la fonction service pour créer le client en utilisant les données reçues
        new_client = create_client(db, client_data.model_dump())
        return new_client  # Retourne le client créé
    except Exception as e:
        # Si une erreur se produit lors de la création du client, renvoie une exception HTTP avec un message d'erreur
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An error occurred while creating the client: {str(e)}"
        )


@router_client.put("/{id}", response_model=ClientResponse, status_code=status.HTTP_200_OK, tags=["Clients"])
def update_client_data(id: int, updated_data: ClientCreate, db: Session = Depends(get_db)):
    """
    Met à jour les informations d'un client existant en fonction de son ID.
    :param id: ID du client à mettre à jour
    :param updated_data: Nouvelles données pour le client
    :param db: Session de base de données
    :return: Le client mis à jour
    """
    try:
        # Appelle la fonction service pour mettre à jour le client avec les nouvelles données
        updated_client = update_client(db, id, updated_data.dict())
        if not updated_client:
            # Si le client n'est pas trouvé, renvoie une erreur HTTP 404
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
        return updated_client  # Retourne le client mis à jour
    except Exception as e:
        # Si une erreur se produit lors de la mise à jour du client, renvoie une exception HTTP avec un message d'erreur
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the client: {str(e)}"
        )


@router_client.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Clients"])
def remove_client(id: int, db: Session = Depends(get_db)):
    """
    Supprime un client de la base de données en fonction de son ID.
    :param id: ID du client à supprimer
    :param db: Session de base de données
    :return: Aucune donnée, seulement un code HTTP 204 en cas de succès
    """
    client = get_by_id(db, id)  # Vérifie si le client existe
    if not client:
        # Si le client n'est pas trouvé, renvoie une erreur HTTP 404 avec un message
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client with ID {id} not found."
        )
    try:
        # Appelle la fonction service pour supprimer le client
        delete_client(db, id)
    except Exception as e:
        # Si une erreur se produit lors de la suppression du client, renvoie une exception HTTP avec un message d'erreur
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the client: {str(e)}"
        )
