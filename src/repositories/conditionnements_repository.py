from sqlalchemy.orm import Session  # Importation de Session pour interagir avec la base de données
from src.models import Conditionnement  # Importation du modèle Conditionnement depuis le module models


# Fonction pour obtenir tous les conditionnements
def get_all_conditionnements(db: Session):
    """
    Récupère tous les conditionnements depuis la base de données.
    :param db: Session de base de données
    :return: Liste de tous les conditionnements
    """
    return db.query(Conditionnement).all()  # Récupère tous les conditionnements de la base de données


# Fonction pour obtenir un conditionnement par son ID
def get_conditionnement_by_id(db: Session, idcondit: int):
    """
    Récupère un conditionnement en fonction de son ID.
    :param db: Session de base de données
    :param idcondit: Identifiant du conditionnement à récupérer
    :return: Le conditionnement correspondant à l'ID ou None si le conditionnement n'existe pas
    """
    return db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()  # Recherche le conditionnement par ID


# Fonction pour créer un nouveau conditionnement
def create_conditionnement(db: Session, conditionnement_data: dict):
    """
    Crée un nouveau conditionnement dans la base de données.
    :param db: Session de base de données
    :param conditionnement_data: Dictionnaire des données du conditionnement (par exemple, type, description, etc.)
    :return: Le conditionnement nouvellement créé
    """
    conditionnement = Conditionnement(**conditionnement_data)  # Crée un nouvel objet Conditionnement avec les données fournies
    db.add(conditionnement)  # Ajoute le conditionnement à la session
    db.commit()  # Effectue la transaction pour sauvegarder le conditionnement dans la base de données
    db.refresh(conditionnement)  # Rafraîchit l'objet pour récupérer l'état mis à jour
    return conditionnement  # Retourne le conditionnement nouvellement créé


# Fonction pour mettre à jour un conditionnement
def update_conditionnement(db: Session, idcondit: int, updated_data: dict):
    """
    Met à jour un conditionnement en fonction de son ID et des nouvelles données.
    :param db: Session de base de données
    :param idcondit: Identifiant du conditionnement à mettre à jour
    :param updated_data: Dictionnaire contenant les nouvelles données pour le conditionnement
    :return: Le conditionnement mis à jour ou None si le conditionnement n'existe pas
    """
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()  # Recherche le conditionnement par ID
    if not conditionnement:  # Si le conditionnement n'existe pas
        return None  # Retourne None si le conditionnement n'a pas été trouvé
    
    # Mise à jour des attributs du conditionnement
    for key, value in updated_data.items():  # Parcourt les nouvelles données
        if hasattr(conditionnement, key):  # Vérifie si l'attribut existe sur l'objet conditionnement
            setattr(conditionnement, key, value)  # Met à jour l'attribut avec la nouvelle valeur
    
    db.commit()  # Effectue la transaction pour valider la mise à jour
    db.refresh(conditionnement)  # Rafraîchit l'objet pour obtenir l'état mis à jour
    return conditionnement  # Retourne le conditionnement mis à jour


# Fonction pour supprimer un conditionnement
def delete_conditionnement(db: Session, idcondit: int):
    """
    Supprime un conditionnement en fonction de son ID.
    :param db: Session de base de données
    :param idcondit: Identifiant du conditionnement à supprimer
    :return: Le conditionnement supprimé si trouvé, sinon None
    """
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()  # Recherche le conditionnement par ID
    if conditionnement:  # Si le conditionnement existe
        db.delete(conditionnement)  # Supprime le conditionnement de la session
        db.commit()  # Effectue la transaction pour valider la suppression
    return conditionnement  # Retourne le conditionnement supprimé ou None si non trouvé
