from fastapi import APIRouter, HTTPException, Depends, status  # Importation de FastAPI et des exceptions HTTP
from src.models import Utilisateur # Importation du modèle utilisateur pour interagir avec la base de données
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données via SQLAlchemy
from typing import List  # Pour spécifier que nous retournons une liste d'objets dans les réponses
from src.database import get_db  # Importation de la fonction pour récupérer une session de base de données
from src.services.utilisateurs_services import get_all_utilisateurs, get_utilisateur_by_id, create_utilisateur, update_utilisateur, delete_utilisateur  # Importation des services
from src.schemas.utilisateur import UtilisateurCreate, UtilisateurResponse  # Importation des schémas de données pour la validation des entrées et sorties

router_utilisateur = APIRouter()  # Création d'un routeur pour les routes liées aux utilisateurs


@router_utilisateur.get("/", response_model=List[UtilisateurResponse], tags=["Utilisateurs"])
def get_utilisateurs(db: Session = Depends(get_db)):
    """
    Récupère tous les utilisateurs depuis la base de données.
    :param db: Session de base de données
    :return: Liste de utilisateurs
    """
    try:
        utilisateurs = get_all_utilisateurs(db)  # Récupère tous les utilisateurs via la fonction service
        return utilisateurs  # Retourne les utilisateurs récupérés
    except Exception as e:
        # Si une erreur se produit lors de la récupération des utilisateurs, renvoie une exception HTTP avec un message d'erreur
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching utilisateurs: {str(e)}"
        )


@router_utilisateur.get("/{id}", response_model=UtilisateurResponse, tags=["Utilisateurs"])
def get_utilisateur_by_id(id: int, db: Session = Depends(get_db)):
    """
    Récupère un utilisateur spécifique en fonction de son ID.
    :param id: ID du utilisateur
    :param db: Session de base de données
    :return: Le utilisateur correspondant à l'ID
    """
    utilisateur = get_utilisateur_by_id(db, id)  # Récupère le utilisateur via la fonction service
    if not utilisateur:
        # Si le utilisateur n'est pas trouvé, renvoie une erreur HTTP 404 avec un message
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"utilisateur with ID {id} not found."
        )
    return utilisateur  # Retourne le utilisateur trouvé


@router_utilisateur.post("/", response_model=UtilisateurResponse, status_code=status.HTTP_201_CREATED, tags=["Utilisateurs"])
def add_utilisateur(utilisateur_data: UtilisateurCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau utilisateur dans la base de données.
    :param utilisateur_data: Données du utilisateur à créer
    :param db: Session de base de données
    :return: Le utilisateur créé
    """
    try:
        # Appelle la fonction service pour créer le utilisateur en utilisant les données reçues
        new_utilisateur = create_utilisateur(db, utilisateur_data.model_dump())
        return new_utilisateur  # Retourne le utilisateur créé
    except Exception as e:
        # Si une erreur se produit lors de la création du utilisateur, renvoie une exception HTTP avec un message d'erreur
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An error occurred while creating the utilisateur: {str(e)}"
        )


@router_utilisateur.put("/{id}", response_model=UtilisateurResponse, status_code=status.HTTP_200_OK, tags=["Utilisateurs"])
def update_utilisateur_data(id: int, updated_data: UtilisateurCreate, db: Session = Depends(get_db)):
    """
    Met à jour les informations d'un utilisateur existant en fonction de son ID.
    :param id: ID du utilisateur à mettre à jour
    :param updated_data: Nouvelles données pour le utilisateur
    :param db: Session de base de données
    :return: Le utilisateur mis à jour
    """
    try:
        # Appelle la fonction service pour mettre à jour le utilisateur avec les nouvelles données
        updated_utilisateur = update_utilisateur(db, id, updated_data.model_dump())
        if not updated_utilisateur:
            # Si le utilisateur n'est pas trouvé, renvoie une erreur HTTP 404
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="utilisateur not found")
        return updated_utilisateur  # Retourne le utilisateur mis à jour
    except Exception as e:
        # Si une erreur se produit lors de la mise à jour du utilisateur, renvoie une exception HTTP avec un message d'erreur
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the utilisateur: {str(e)}"
        )


@router_utilisateur.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Utilisateurs"])
def remove_utilisateur(id: int, db: Session = Depends(get_db)):
    """
    Supprime un utilisateur de la base de données en fonction de son ID.
    :param id: ID du utilisateur à supprimer
    :param db: Session de base de données
    :return: Aucune donnée, seulement un code HTTP 204 en cas de succès
    """
    utilisateur = get_utilisateur_by_id(db, id)  # Vérifie si le utilisateur existe
    if not utilisateur:
        # Si le utilisateur n'est pas trouvé, renvoie une erreur HTTP 404 avec un message
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"utilisateur with ID {id} not found."
        )
    try:
        # Appelle la fonction service pour supprimer le utilisateur
        delete_utilisateur(db, id)
    except Exception as e:
        # Si une erreur se produit lors de la suppression du utilisateur, renvoie une exception HTTP avec un message d'erreur
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the utilisateur: {str(e)}"
        )
