# repositories/commune.py
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données
from src.models import Commune  # Importation du modèle Commune depuis le module models


# Fonction pour obtenir toutes les communes
def get_all_communes(db: Session):
    """
    Récupère toutes les communes depuis la base de données.
    :param db: Session de base de données
    :return: Liste de toutes les communes
    """
    return db.query(Commune).all()  # Exécute une requête pour récupérer toutes les communes


# Fonction pour obtenir une commune par son ID
def get_commune_by_id(db: Session, id: int):
    """
    Récupère une commune en fonction de son ID.
    :param db: Session de base de données
    :param id: Identifiant de la commune à récupérer
    :return: La commune correspondant à l'ID ou None si la commune n'existe pas
    """
    return db.query(Commune).filter(Commune.id == id).first()  # Recherche la commune par ID


# Fonction pour créer une nouvelle commune
def create_commune(db: Session, commune_data: dict):
    """
    Crée une nouvelle commune dans la base de données.
    :param db: Session de base de données
    :param commune_data: Dictionnaire des données de la commune (par exemple, nom, région, etc.)
    :return: La commune nouvellement créée
    """
    if len(commune_data.get('dep', '')) > 2:
        raise ValueError("Le code 'dep' ne doit pas dépasser 2 caractères.")
    commune = Commune(**commune_data)
    db.add(commune)
    db.commit()
    db.refresh(commune)
    return commune


# Fonction pour mettre à jour une commune
def update_commune(db: Session, id: int, updated_data: dict):
    """
    Met à jour une commune en fonction de son ID et des nouvelles données.
    :param db: Session de base de données
    :param id: Identifiant de la commune à mettre à jour
    :param updated_data: Dictionnaire contenant les nouvelles données pour la commune
    :return: La commune mise à jour ou None si la commune n'existe pas
    """
    commune = db.query(Commune).filter(Commune.id == id).first()  # Recherche la commune par ID
    if not commune:  # Si la commune n'existe pas
        return None  # Retourne None si la commune n'est pas trouvée
    
    # Mise à jour des attributs de la commune
    for key, value in updated_data.items():  # Parcourt les nouvelles données
        if hasattr(commune, key):  # Vérifie si la commune a cet attribut
            setattr(commune, key, value)  # Met à jour l'attribut avec la nouvelle valeur
    
    db.commit()  # Effectue la transaction pour valider la mise à jour
    db.refresh(commune)  # Rafraîchit l'objet pour obtenir l'état mis à jour
    return commune  # Retourne la commune mise à jour


# Fonction pour supprimer une commune
def delete_commune(db: Session, id: int):
    """
    Supprime une commune en fonction de son ID.
    :param db: Session de base de données
    :param id: Identifiant de la commune à supprimer
    :return: La commune supprimée si elle a été trouvée, sinon None
    """
    commune = db.query(Commune).filter(Commune.id == id).first()  # Recherche la commune par ID
    if commune:  # Si la commune existe
        db.delete(commune)  # Supprime la commune de la session
        db.commit()  # Effectue la transaction pour valider la suppression
    return commune  # Retourne la commune supprimée ou None si elle n'existe pas
