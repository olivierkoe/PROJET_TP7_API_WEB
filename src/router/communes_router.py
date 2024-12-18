from fastapi import APIRouter, Depends, HTTPException, status  # Importation des outils FastAPI
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données via SQLAlchemy
from src.services.communes_services import (
    fetch_all_communes,            # Service pour récupérer toutes les communes
    fetch_commune_by_id,           # Service pour récupérer une commune par son ID
    add_commune,                   # Service pour ajouter une nouvelle commune
    modify_commune,                # Service pour modifier une commune existante
    remove_commune                 # Service pour supprimer une commune
)
from src.schemas.commune import Commune, CommuneCreate  # Importation des schémas de validation des données
from src.database import get_db  # Importation de la fonction pour obtenir la session de base de données

# Initialisation du routeur pour gérer les routes relatives aux communes
router_commune = APIRouter()


# Route pour récupérer toutes les communes
@router_commune.get("/", response_model=list[Commune], tags=["Communes"])
def get_communes(db: Session = Depends(get_db)):
    """
    Récupère toutes les communes depuis la base de données.
    :param db: Session de base de données
    :return: Liste de toutes les communes
    """
    return fetch_all_communes(db)  # Appelle la fonction de service pour récupérer toutes les communes


# Route pour récupérer une commune spécifique par ID
@router_commune.get("/{id}", response_model=Commune, tags=["Communes"])
def get_commune(id: int, db: Session = Depends(get_db)):
    """
    Récupère une commune spécifique par son ID.
    :param id: L'ID de la commune à récupérer
    :param db: Session de base de données
    :return: La commune avec l'ID spécifié
    """
    commune = fetch_commune_by_id(db, id)  # Appelle la fonction de service pour récupérer une commune par ID
    if not commune:
        # Si la commune n'est pas trouvée, renvoie une erreur HTTP 404 (non trouvée)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    return commune  # Retourne la commune trouvée


# Route pour créer une nouvelle commune
@router_commune.post("/", response_model=Commune, status_code=status.HTTP_201_CREATED, tags=["Communes"])
def create_commune(commune_data: CommuneCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle commune dans la base de données.
    :param commune_data: Données de la commune à créer
    :param db: Session de base de données
    :return: La commune nouvellement créée
    """
    return add_commune(db, commune_data.dict())  # Appelle la fonction de service pour ajouter une commune


# Route pour mettre à jour une commune existante par son ID
@router_commune.put("/{id}", response_model=Commune, tags=["Communes"])
def update_commune(id: int, updated_data: dict, db: Session = Depends(get_db)):
    """
    Met à jour une commune existante en fonction de son ID.
    :param id: L'ID de la commune à mettre à jour
    :param updated_data: Données mises à jour pour la commune
    :param db: Session de base de données
    :return: La commune mise à jour
    """
    commune = modify_commune(db, id, updated_data)  # Appelle la fonction de service pour modifier la commune
    if not commune:
        # Si la commune n'est pas trouvée, renvoie une erreur HTTP 404 (non trouvée)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    return commune  # Retourne la commune mise à jour


# Route pour supprimer une commune par ID
@router_commune.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Communes"])
def delete_commune(id: int, db: Session = Depends(get_db)):
    """
    Supprime une commune en fonction de son ID.
    :param id: L'ID de la commune à supprimer
    :param db: Session de base de données
    :return: Message de succès de suppression
    """
    commune = remove_commune(db, id)  # Appelle la fonction de service pour supprimer la commune
    if not commune:
        # Si la commune n'est pas trouvée, renvoie une erreur HTTP 404 (non trouvée)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commune not found")
    # Retourne une réponse vide avec un code de statut 204 pour indiquer que la suppression a réussi
