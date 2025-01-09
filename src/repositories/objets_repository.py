# repositories/objets_repositories.py
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données
from models import Objet  # Importation du modèle Objet depuis le module models


# Créer un objet
def create_objet(db: Session, objet_data: dict):
    """
    Crée un nouvel objet dans la base de données.
    :param db: Session de base de données
    :param objet_data: Données de l'objet sous forme de dictionnaire
    :return: L'objet nouvellement créé
    """
    objet = Objet(**objet_data)  # Crée un nouvel objet Objet avec les données fournies
    db.add(objet)  # Ajoute l'objet à la session
    db.commit()  # Effectue la transaction pour sauvegarder l'objet dans la base de données
    db.refresh(objet)  # Rafraîchit l'objet pour récupérer l'état mis à jour
    return objet  # Retourne l'objet nouvellement créé


# Récupérer un objet par son ID
def get_objet_by_id(db: Session, codobj: int):
    """
    Récupère un objet en fonction de son ID.
    :param db: Session de base de données
    :param codobj: Identifiant de l'objet à récupérer
    :return: L'objet correspondante ou None si l'objet n'existe pas
    """
    return db.query(Objet).filter(Objet.codobj == codobj).first()  # Recherche l'objet par ID


# Récupérer tous les objets
def get_all_objets(db: Session):
    """
    Récupère tous les objets depuis la base de données.
    :param db: Session de base de données
    :return: Liste de tous les objets
    """
    return db.query(Objet).all()  # Récupère tous les objets


# Supprimer un objet
def delete_objet(db: Session, codobj: int):
    """
    Supprime un objet en fonction de son ID.
    :param db: Session de base de données
    :param codobj: Identifiant de l'objet à supprimer
    """
    objet = db.query(Objet).filter(Objet.codobj == codobj).first()  # Recherche l'objet par ID
    if objet:  # Si l'objet est trouvé
        db.delete(objet)  # Supprime l'objet de la session
        db.commit()  # Effectue la transaction pour valider la suppression


# Mettre à jour un objet
def update_objet(db: Session, codobj: int, updated_data: dict):
    """
    Met à jour un objet en fonction de son ID et des nouvelles données.
    :param db: Session de base de données
    :param codobj: Identifiant de l'objet à mettre à jour
    :param updated_data: Dictionnaire contenant les nouvelles données pour l'objet
    :return: L'objet mis à jour ou None si l'objet n'existe pas
    """
    objet = db.query(Objet).filter(Objet.codobj == codobj).first()  # Recherche l'objet par ID
    if objet:  # Si l'objet existe
        for key, value in updated_data.items():  # Parcourt les données mises à jour
            if hasattr(objet, key):  # Si l'attribut existe sur l'objet
                setattr(objet, key, value)  # Met à jour l'attribut avec la nouvelle valeur
        db.commit()  # Effectue la transaction pour valider la mise à jour
        db.refresh(objet)  # Rafraîchit l'objet pour obtenir l'état mis à jour
        return objet  # Retourne l'objet mis à jour
    return None  # Retourne None si l'objet n'a pas été trouvé
