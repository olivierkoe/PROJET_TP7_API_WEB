from fastapi import APIRouter, Depends, HTTPException, status  # Importation de FastAPI et des exceptions HTTP
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données via SQLAlchemy
from services.commandes_services import (
    create_commande,           # Service pour créer une commande
    get_all_commandes,         # Service pour récupérer toutes les commandes
    get_commande_by_id,        # Service pour récupérer une commande par son ID
    update_commande,           # Service pour mettre à jour une commande
    delete_commande            # Service pour supprimer une commande
)
from schemas.commande import CommandeCreate, CommandeResponse  # Importation des schémas de données pour la validation des entrées et sorties
from database import get_db  # Importation de la fonction pour récupérer une session de base de données

# Définir le routeur pour les commandes
router_commande = APIRouter()  # Création d'un routeur pour les routes liées aux commandes


# Route pour créer une nouvelle commande
@router_commande.post("/", response_model=CommandeResponse, status_code=status.HTTP_201_CREATED)
def create_new_commande(commande_data: CommandeCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle commande dans la base de données.
    :param commande_data: Données de la commande à créer
    :param db: Session de base de données
    :return: La commande nouvellement créée
    """
    return create_commande(db=db, commande_data=commande_data)  # Appelle la fonction service pour créer la commande


# Route pour récupérer toutes les commandes
@router_commande.get("/", response_model=list[CommandeResponse])
def get_all(db: Session = Depends(get_db)):
    """
    Récupère toutes les commandes depuis la base de données.
    :param db: Session de base de données
    :return: Liste de toutes les commandes
    """
    return get_all_commandes(db)  # Appelle la fonction service pour récupérer toutes les commandes


# Route pour récupérer une commande par ID
@router_commande.get("/{codcde}", response_model=CommandeResponse)
def get_by_id(codcde: int, db: Session = Depends(get_db)):
    """
    Récupère une commande spécifique en fonction de son ID.
    :param codcde: L'ID de la commande à récupérer
    :param db: Session de base de données
    :return: La commande correspondant à l'ID
    """
    commande = get_commande_by_id(db=db, codcde=codcde)  # Appelle la fonction service pour récupérer la commande par ID
    if not commande:
        # Si la commande n'est pas trouvée, renvoie une erreur HTTP 404 (commande non trouvée)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    return commande  # Retourne la commande trouvée


# Route pour mettre à jour une commande par ID
@router_commande.put("/{codcde}", response_model=CommandeResponse)
def update_commande_by_id(codcde: int, updated_data: CommandeCreate, db: Session = Depends(get_db)):
    """
    Met à jour une commande en fonction de son ID.
    :param codcde: L'ID de la commande à mettre à jour
    :param updated_data: Données mises à jour pour la commande
    :param db: Session de base de données
    :return: La commande mise à jour
    """
    commande = update_commande(db=db, codcde=codcde, updated_data=updated_data)  # Appelle la fonction service pour mettre à jour la commande
    if not commande:
        # Si la commande n'est pas trouvée, renvoie une erreur HTTP 404 (commande non trouvée)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    return commande  # Retourne la commande mise à jour


# Route pour supprimer une commande par ID
@router_commande.delete("/{codcde}", status_code=status.HTTP_204_NO_CONTENT)
def delete_commande_by_id(codcde: int, db: Session = Depends(get_db)):
    """
    Supprime une commande en fonction de son ID.
    :param codcde: L'ID de la commande à supprimer
    :param db: Session de base de données
    :return: Message de succès de suppression
    """
    commande = get_commande_by_id(db=db, codcde=codcde)  # Vérifie si la commande existe
    if not commande:
        # Si la commande n'est pas trouvée, renvoie une erreur HTTP 404 (commande non trouvée)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande not found")
    
    delete_commande(db=db, codcde=codcde)  # Appelle la fonction service pour supprimer la commande
    return {"message": "Commande deleted successfully"}  # Retourne un message de succès
