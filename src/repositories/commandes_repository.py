# repositories/commandes_repositories.py
from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données
from models import Commande  # Importation du modèle Commande depuis le module models


# Créer une commande
def create_commande(db: Session, commande_data: dict):
    """
    Crée une nouvelle commande dans la base de données.
    :param db: Session de base de données
    :param commande_data: Données de la commande sous forme de dictionnaire
    :return: La commande nouvellement créée
    """
    commande = Commande(**commande_data)  # Crée un nouvel objet Commande avec les données fournies
    db.add(commande)  # Ajoute la commande à la session
    db.commit()  # Effectue la transaction pour sauvegarder la commande dans la base de données
    db.refresh(commande)  # Rafraîchit l'objet commande pour récupérer l'état mis à jour
    return commande  # Retourne la commande nouvellement créée


# Récupérer une commande par son ID
def get_commande_by_id(db: Session, codcde: int):
    """
    Récupère une commande en fonction de son ID.
    :param db: Session de base de données
    :param codcde: Identifiant de la commande à récupérer
    :return: La commande correspondante ou None si la commande n'existe pas
    """
    return db.query(Commande).filter(Commande.codcde == codcde).first()  # Recherche la commande par ID


# Récupérer toutes les commandes
def get_all_commandes(db: Session):
    """
    Récupère toutes les commandes depuis la base de données.
    :param db: Session de base de données
    :return: Liste de toutes les commandes
    """
    return db.query(Commande).all()  # Récupère toutes les commandes


# Supprimer une commande
def delete_commande(db: Session, codcde: int):
    """
    Supprime une commande en fonction de son ID.
    :param db: Session de base de données
    :param codcde: Identifiant de la commande à supprimer
    """
    commande = db.query(Commande).filter(Commande.codcde == codcde).first()  # Recherche la commande par ID
    if commande:  # Si la commande est trouvée
        db.delete(commande)  # Supprime la commande de la session
        db.commit()  # Effectue la transaction pour valider la suppression


# Mettre à jour une commande
def update_commande(db: Session, codcde: int, updated_data: dict):
    """
    Met à jour une commande en fonction de son ID et des nouvelles données.
    :param db: Session de base de données
    :param codcde: Identifiant de la commande à mettre à jour
    :param updated_data: Dictionnaire contenant les nouvelles données pour la commande
    :return: La commande mise à jour ou None si la commande n'existe pas
    """
    commande = db.query(Commande).filter(Commande.codcde == codcde).first()  # Recherche la commande par ID
    if commande:  # Si la commande existe
        for key, value in updated_data.items():  # Parcourt les données mises à jour
            if hasattr(commande, key):  # Si l'attribut existe sur l'objet commande
                setattr(commande, key, value)  # Met à jour l'attribut avec la nouvelle valeur
        db.commit()  # Effectue la transaction pour valider la mise à jour
        db.refresh(commande)  # Rafraîchit l'objet pour obtenir l'état mis à jour
        return commande  # Retourne la commande mise à jour
    return None  # Retourne None si la commande n'a pas été trouvée
