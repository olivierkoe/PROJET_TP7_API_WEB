from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données
from models import Departement  # Importation du modèle Departement depuis le module models


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
    :return: Le département correspondant au code, ou une exception si le département n'existe pas
    """
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()  # Recherche le département par son code
    if not departement:  # Si le département n'est pas trouvé
        raise ValueError(f"Département avec le code '{code_dept}' introuvable.")  # Lève une exception si le département n'existe pas
    return departement  # Retourne le département trouvé


# Fonction pour créer un nouveau département
def create_departement(db: Session, departement_data: DepartementCreate):
    """
    Crée un nouveau département dans la base de données.
    :param db: Session de base de données
    :param departement_data: Dictionnaire ou objet contenant les données du département à créer
    :return: Le département nouvellement créé
    """
    # Affiche les données reçues avant la conversion
    print(f"Received departement data: {departement_data}")
    
    departement_dict = departement_data.dict()  # Convertit les données en dictionnaire
    print(f"Converted to dict: {departement_dict}")  # Affiche les données après conversion
    
    departement = Departement(**departement_dict)  # Crée un objet Departement à partir des données
    db.add(departement)  # Ajoute le département à la session
    db.commit()  # Effectue la transaction pour sauvegarder le département dans la base de données
    db.refresh(departement)  # Rafraîchit l'objet pour récupérer l'état mis à jour
    return departement  # Retourne le département créé


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
