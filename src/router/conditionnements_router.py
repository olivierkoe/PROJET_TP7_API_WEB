from fastapi import APIRouter, Depends, HTTPException, status  # Importation des outils FastAPI
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données via SQLAlchemy
from services.conditionnements_services import (
    fetch_all_conditionnements,           # Service pour récupérer tous les conditionnements
    fetch_conditionnement_by_id,          # Service pour récupérer un conditionnement par son ID
    add_conditionnement,                  # Service pour ajouter un nouveau conditionnement
    modify_conditionnement,               # Service pour modifier un conditionnement existant
    remove_conditionnement                # Service pour supprimer un conditionnement
)
from schemas.conditionnement import Conditionnement, ConditionnementCreate  # Importation des schémas de validation des données
from database import get_db  # Importation de la fonction pour obtenir la session de base de données

# Initialisation du routeur pour gérer les routes relatives aux conditionnements
router_conditionnement = APIRouter()

# Route pour récupérer tous les conditionnements
@router_conditionnement.get("/", response_model=list[Conditionnement], tags=["Conditionnements"])
def get_conditionnements(db: Session = Depends(get_db)):
    """
    Récupère tous les conditionnements depuis la base de données.
    :param db: Session de base de données
    :return: Liste de tous les conditionnements
    """
    return fetch_all_conditionnements(db)  # Appelle la fonction de service pour récupérer tous les conditionnements


# Route pour récupérer un conditionnement spécifique par ID
@router_conditionnement.get("/{idcondit}", response_model=Conditionnement, tags=["Conditionnements"])
def get_conditionnement(idcondit: int, db: Session = Depends(get_db)):
    """
    Récupère un conditionnement spécifique par son ID.
    :param idcondit: L'ID du conditionnement à récupérer
    :param db: Session de base de données
    :return: Le conditionnement avec l'ID spécifié
    """
    conditionnement = fetch_conditionnement_by_id(db, idcondit)  # Appelle la fonction de service pour récupérer un conditionnement par ID
    if not conditionnement:
        # Si le conditionnement n'est pas trouvé, renvoie une erreur HTTP 404 (non trouvé)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    return conditionnement  # Retourne le conditionnement trouvé


# Route pour créer un nouveau conditionnement
@router_conditionnement.post("/", response_model=Conditionnement, status_code=status.HTTP_201_CREATED, tags=["Conditionnements"])
def create_conditionnement(conditionnement_data: ConditionnementCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau conditionnement dans la base de données.
    :param conditionnement_data: Données du conditionnement à créer
    :param db: Session de base de données
    :return: Le conditionnement nouvellement créé
    """
    return add_conditionnement(db, conditionnement_data.dict())  # Appelle la fonction de service pour ajouter un conditionnement


# Route pour mettre à jour un conditionnement existant par son ID
@router_conditionnement.put("/{idcondit}", response_model=Conditionnement, tags=["Conditionnements"])
def update_conditionnement(idcondit: int, updated_data: dict, db: Session = Depends(get_db)):
    """
    Met à jour un conditionnement existant en fonction de son ID.
    :param idcondit: L'ID du conditionnement à mettre à jour
    :param updated_data: Données mises à jour pour le conditionnement
    :param db: Session de base de données
    :return: Le conditionnement mis à jour
    """
    conditionnement = modify_conditionnement(db, idcondit, updated_data)  # Appelle la fonction de service pour modifier un conditionnement
    if not conditionnement:
        # Si le conditionnement n'est pas trouvé, renvoie une erreur HTTP 404 (non trouvé)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    return conditionnement  # Retourne le conditionnement mis à jour


# Route pour supprimer un conditionnement par ID
@router_conditionnement.delete("/{idcondit}", status_code=status.HTTP_204_NO_CONTENT, tags=["Conditionnements"])
def delete_conditionnement(idcondit: int, db: Session = Depends(get_db)):
    """
    Supprime un conditionnement en fonction de son ID.
    :param idcondit: L'ID du conditionnement à supprimer
    :param db: Session de base de données
    :return: Message de succès de suppression
    """
    conditionnement = remove_conditionnement(db, idcondit)  # Appelle la fonction de service pour supprimer un conditionnement
    if not conditionnement:
        # Si le conditionnement n'est pas trouvé, renvoie une erreur HTTP 404 (non trouvé)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conditionnement not found")
    # Retourne une réponse vide avec un code de statut 204 pour indiquer que la suppression a réussi
