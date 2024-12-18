from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.departements_services import (
    get_all,  # Fonction pour récupérer tous les départements
    get_by_id,  # Fonction pour récupérer un département par son code
    create_departement,  # Fonction pour créer un département
    delete_departement,  # Fonction pour supprimer un département
    update_departement,  # Fonction pour mettre à jour un département
)
from src.schemas.departement import DepartementCreate, Departement  # Correction des imports

# Initialisation du routeur pour les départements
router_departement = APIRouter()

# Route pour récupérer tous les départements
@router_departement.get("/", status_code=status.HTTP_200_OK, response_model=list[Departement], tags=["Départements"])
def get_departements(db: Session = Depends(get_db)):
    """
    Cette route récupère tous les départements depuis la base de données.
    En cas d'erreur, une exception HTTP 500 est levée avec le message d'erreur.
    """
    try:
        departements = get_all(db)  # Récupère tous les départements via le service
        return departements  # Retourne la liste des départements
    except Exception as e:
        # Si une erreur se produit, retourne une erreur HTTP 500
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Route pour récupérer un département par son code
@router_departement.get("/{code_dept}", status_code=status.HTTP_200_OK, response_model=Departement, tags=["Départements"])
def get_departement(code_dept: str, db: Session = Depends(get_db)):
    """
    Cette route récupère un département spécifique à partir de son code (code_dept).
    Si le département n'est pas trouvé, une exception HTTP 404 est levée.
    """
    try:
        departement = get_by_id(db, code_dept)  # Récupère le département via le service
        if not departement:
            # Si le département n'existe pas, lève une exception HTTP 404
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Département non trouvé")
        return departement  # Retourne le département trouvé
    except Exception as e:
        # Si une autre erreur se produit, retourne une erreur HTTP 500
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Route pour ajouter un nouveau département
@router_departement.post("/", status_code=status.HTTP_201_CREATED, response_model=Departement, tags=["Départements"])
def add_departement(departement_data: DepartementCreate, db: Session = Depends(get_db)):
    """
    Cette route permet de créer un nouveau département dans la base de données.
    Si une erreur se produit pendant la création, une exception HTTP 400 est levée.
    """
    try:
        # Crée un nouveau département via le service
        return create_departement(db, departement_data)
    except Exception as e:
        # Si une erreur se produit, retourne une erreur HTTP 400
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# Route pour modifier un département existant
@router_departement.put("/{code_dept}", status_code=status.HTTP_200_OK, response_model=Departement, tags=["Départements"])
def modify_departement(code_dept: str, updated_data: DepartementCreate, db: Session = Depends(get_db)):
    """
    Cette route permet de mettre à jour les données d'un département existant.
    Si le département n'est pas trouvé, une exception HTTP 404 est levée.
    En cas d'autres erreurs, une exception HTTP 500 est levée.
    """
    try:
        # Met à jour le département via le service
        return update_departement(db, code_dept, updated_data.dict())
    except ValueError as ve:
        # Si le département n'existe pas, lève une exception HTTP 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ve))
    except Exception as e:
        # Si une autre erreur se produit, retourne une erreur HTTP 500
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Route pour supprimer un département
@router_departement.delete("/{code_dept}", status_code=status.HTTP_204_NO_CONTENT, tags=["Départements"])
def remove_departement(code_dept: str, db: Session = Depends(get_db)):
    """
    Cette route permet de supprimer un département en utilisant son code (code_dept).
    Si le département n'est pas trouvé, une exception HTTP 404 est levée.
    En cas d'autres erreurs, une exception HTTP 500 est levée.
    """
    try:
        # Supprime le département via le service
        delete_departement(db, code_dept)
    except ValueError as ve:
        # Si le département n'existe pas, lève une exception HTTP 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ve))
    except Exception as e:
        # Si une autre erreur se produit, retourne une erreur HTTP 500
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
