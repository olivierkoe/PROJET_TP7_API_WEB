# routers/objets_router.py
from fastapi import APIRouter, Depends, HTTPException, status  # Importation de FastAPI et des exceptions HTTP
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données via SQLAlchemy
from src.services.objets_services import (
    create_objet,            # Service pour créer un objet
    get_all_objets,          # Service pour récupérer tous les objets
    get_objet_by_id,         # Service pour récupérer un objet par son ID
    update_objet,            # Service pour mettre à jour un objet
    delete_objet             # Service pour supprimer un objet
)
from src.schemas.objet import ObjetCreate, ObjetResponse  # Importation des schémas de données pour la validation des entrées et sorties
from src.database import get_db  # Importation de la fonction pour récupérer une session de base de données

# Définir le routeur pour les objets
router_objet = APIRouter()  # Création d'un routeur pour les routes liées aux objets


# Route pour créer un nouvel objet
@router_objet.post("/", response_model=ObjetResponse, status_code=status.HTTP_201_CREATED)
def create_new_objet(objet_data: ObjetCreate, db: Session = Depends(get_db)):
    """
    Crée un nouvel objet dans la base de données.
    :param objet_data: Données de l'objet à créer
    :param db: Session de base de données
    :return: L'objet nouvellement créé
    """
    return create_objet(db=db, objet_data=objet_data)  # Appelle la fonction service pour créer l'objet


# Route pour récupérer tous les objets
@router_objet.get("/", response_model=list[ObjetResponse])
def get_all(db: Session = Depends(get_db)):
    """
    Récupère tous les objets depuis la base de données.
    :param db: Session de base de données
    :return: Liste de tous les objets
    """
    return get_all_objets(db)  # Appelle la fonction service pour récupérer tous les objets


# Route pour récupérer un objet par ID
@router_objet.get("/{codobj}", response_model=ObjetResponse)
def get_by_id(codobj: int, db: Session = Depends(get_db)):
    """
    Récupère un objet spécifique en fonction de son ID.
    :param codobj: L'ID de l'objet à récupérer
    :param db: Session de base de données
    :return: L'objet correspondant à l'ID
    """
    objet = get_objet_by_id(db=db, codobj=codobj)  # Appelle la fonction service pour récupérer l'objet par ID
    if not objet:
        # Si l'objet n'est pas trouvé, renvoie une erreur HTTP 404 (objet non trouvé)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
    return objet  # Retourne l'objet trouvé


# Route pour mettre à jour un objet par ID
@router_objet.put("/{codobj}", response_model=ObjetResponse)
def update_objet_by_id(codobj: int, updated_data: ObjetCreate, db: Session = Depends(get_db)):
    """
    Met à jour un objet en fonction de son ID.
    :param codobj: L'ID de l'objet à mettre à jour
    :param updated_data: Données mises à jour pour l'objet
    :param db: Session de base de données
    :return: L'objet mis à jour
    """
    objet = update_objet(db=db, codobj=codobj, updated_data=updated_data)  # Appelle la fonction service pour mettre à jour l'objet
    if not objet:
        # Si l'objet n'est pas trouvé, renvoie une erreur HTTP 404 (objet non trouvé)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
    return objet  # Retourne l'objet mis à jour


# Route pour supprimer un objet par ID
@router_objet.delete("/{codobj}", status_code=status.HTTP_204_NO_CONTENT)
def delete_objet_by_id(codobj: int, db: Session = Depends(get_db)):
    """
    Supprime un objet en fonction de son ID.
    :param codobj: L'ID de l'objet à supprimer
    :param db: Session de base de données
    :return: Message de succès de suppression
    """
    objet = get_objet_by_id(db=db, codobj=codobj)  # Vérifie si l'objet existe
    if not objet:
        # Si l'objet n'est pas trouvé, renvoie une erreur HTTP 404 (objet non trouvé)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Objet not found")
    
    delete_objet(db=db, codobj=codobj)  # Appelle la fonction service pour supprimer l'objet
    return {"message": "Objet deleted successfully"}  # Retourne un message de succès
