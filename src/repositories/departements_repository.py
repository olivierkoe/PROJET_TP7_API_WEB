from fastapi import HTTPException, status

from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données
from src.models import Departement  # Importation du modèle Departement depuis le module models


# Fonction pour obtenir tous les départements
def get_all_departements(db: Session):
    """
    Récupère tous les départements depuis la base de données.
    :param db: Session de base de données
    :return: Liste de tous les départements
    """
    return db.query(Departement).all()  # Récupère tous les départements présents dans la base de données


# Fonction pour obtenir un département par son code
def get_departement_by_id(db: Session, code_dept: str):
    """
    Récupère un département en fonction de son code.
    :param db: Session de base de données
    :param code_dept: Code du département à récupérer
    :return: Le département correspondant au code, ou une exception HTTP 404 si le département n'existe pas
    """
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()  # Recherche le département par son code
    if not departement:  # Si le département n'est pas trouvé
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Département avec le code '{code_dept}' introuvable."
        )  # Lève une exception HTTP 404 si le département n'existe pas
    return departement  # Retourne le département trouvé


# Fonction pour créer un nouveau département
def create_departement(db: Session, departement_data):
    """
    Crée un nouveau département dans la base de données.
    :param db: Session de base de données
    :param departement_data: Données du département à créer (dict ou Pydantic)
    :return: Le département nouvellement créé
    """
    try:
        new_departement = Departement(**departement_data)
        # Ajouter le département à la session
        db.add(new_departement)
        db.commit()
        db.refresh(new_departement)

        return new_departement
    except Exception as e:
        print(f"Erreur lors de la création du département : {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erreur lors de la création : {str(e)}")


# Fonction pour supprimer un département
def delete_departement(db: Session, code_dept: str):
    """
    Supprime un département en fonction de son code.
    :param db: Session de base de données
    :param code_dept: Code du département à supprimer
    :return: Aucun retour, lève une exception si le département n'existe pas
    """
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()  # Recherche le département par son code
    if not departement:  # Si le département n'existe pas
        raise ValueError(f"Département avec le code '{code_dept}' introuvable.")  # Lève une exception si le département n'existe pas
    db.delete(departement)  # Supprime le département de la session
    db.commit()  # Effectue la transaction pour valider la suppression


# Fonction pour mettre à jour un département
def update_departement(db: Session, code_dept: str, updated_data: dict):
    """
    Met à jour un département en fonction de son code et des nouvelles données.
    :param db: Session de base de données
    :param code_dept: Code du département à mettre à jour
    :param updated_data: Dictionnaire contenant les nouvelles données pour le département
    :return: Le département mis à jour, ou une exception si le département n'existe pas
    """
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()  # Recherche le département par son code
    if not departement:  # Si le département n'existe pas
        raise ValueError(f"Département avec le code '{code_dept}' introuvable.")  # Lève une exception si le département n'est pas trouvé
    
    # Mise à jour des attributs du département
    for key, value in updated_data.items():  # Parcourt les données à mettre à jour
        if hasattr(departement, key):  # Vérifie si l'attribut existe sur l'objet departement
            setattr(departement, key, value)  # Met à jour l'attribut avec la nouvelle valeur
    
    db.commit()  # Effectue la transaction pour valider la mise à jour
    db.refresh(departement)  # Rafraîchit l'objet pour récupérer l'état mis à jour
    return departement  # Retourne le département mis à jour
