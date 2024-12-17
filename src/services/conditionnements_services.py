from sqlalchemy.orm import Session
from repositories.conditionnements_repository import (
    get_all_conditionnements,  # Importation de la fonction pour récupérer tous les conditionnements
    get_conditionnement_by_id,  # Importation de la fonction pour récupérer un conditionnement par son ID
    create_conditionnement,  # Importation de la fonction pour créer un nouveau conditionnement
    update_conditionnement,  # Importation de la fonction pour mettre à jour un conditionnement existant
    delete_conditionnement  # Importation de la fonction pour supprimer un conditionnement
)

# Fonction pour récupérer tous les conditionnements
def fetch_all_conditionnements(db: Session):
    """
    Récupère tous les conditionnements présents dans la base de données.
    
    :param db: Session de base de données
    :return: Liste des conditionnements
    """
    # Appelle la fonction du repository pour récupérer tous les conditionnements
    return get_all_conditionnements(db)

# Fonction pour récupérer un conditionnement par son ID
def fetch_conditionnement_by_id(db: Session, idcondit: int):
    """
    Récupère un conditionnement spécifique par son identifiant (ID).
    
    :param db: Session de base de données
    :param idcondit: Identifiant du conditionnement à récupérer
    :return: Le conditionnement correspondante, ou None si non trouvé
    """
    # Appelle la fonction du repository pour récupérer le conditionnement par ID
    return get_conditionnement_by_id(db, idcondit)

# Fonction pour créer un nouveau conditionnement
def add_conditionnement(db: Session, conditionnement_data: dict):
    """
    Crée un nouveau conditionnement dans la base de données avec les données fournies.
    
    :param db: Session de base de données
    :param conditionnement_data: Données du conditionnement à créer sous forme de dictionnaire
    :return: Le conditionnement créé
    """
    # Appelle la fonction du repository pour créer un conditionnement
    return create_conditionnement(db, conditionnement_data)

# Fonction pour mettre à jour un conditionnement
def modify_conditionnement(db: Session, idcondit: int, updated_data: dict):
    """
    Met à jour un conditionnement existant avec les nouvelles données fournies.
    
    :param db: Session de base de données
    :param idcondit: Identifiant du conditionnement à mettre à jour
    :param updated_data: Données mises à jour sous forme de dictionnaire
    :return: Le conditionnement mis à jour, ou None si le conditionnement n'existe pas
    """
    # Appelle la fonction du repository pour mettre à jour le conditionnement
    return update_conditionnement(db, idcondit, updated_data)

# Fonction pour supprimer un conditionnement
def remove_conditionnement(db: Session, idcondit: int):
    """
    Supprime un conditionnement de la base de données par son identifiant (ID).
    
    :param db: Session de base de données
    :param idcondit: Identifiant du conditionnement à supprimer
    :return: None
    """
    # Appelle la fonction du repository pour supprimer le conditionnement
    return delete_conditionnement(db, idcondit)
