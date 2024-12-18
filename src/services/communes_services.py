from sqlalchemy.orm import Session
from src.repositories.communes_repositories import (
    get_all_communes,  # Importation de la fonction pour récupérer toutes les communes
    get_commune_by_id,  # Importation de la fonction pour récupérer une commune par son ID
    create_commune,  # Importation de la fonction pour créer une nouvelle commune
    update_commune,  # Importation de la fonction pour mettre à jour une commune existante
    delete_commune  # Importation de la fonction pour supprimer une commune
)

# Fonction pour récupérer toutes les communes
def fetch_all_communes(db: Session):
    """
    Récupère toutes les communes présentes dans la base de données.
    
    :param db: Session de base de données
    :return: Liste des communes
    """
    # Appelle la fonction du repository pour récupérer toutes les communes
    return get_all_communes(db)

# Fonction pour récupérer une commune par son ID
def fetch_commune_by_id(db: Session, id: int):
    """
    Récupère une commune spécifique par son identifiant (ID).
    
    :param db: Session de base de données
    :param id: Identifiant de la commune à récupérer
    :return: La commune correspondante, ou None si non trouvée
    """
    # Appelle la fonction du repository pour récupérer la commune par ID
    return get_commune_by_id(db, id)

# Fonction pour créer une nouvelle commune
def add_commune(db: Session, commune_data: dict):
    """
    Crée une nouvelle commune dans la base de données avec les données fournies.
    
    :param db: Session de base de données
    :param commune_data: Données de la commune à créer sous forme de dictionnaire
    :return: La commune créée
    """
    # Appelle la fonction du repository pour créer une commune
    return create_commune(db, commune_data)

# Fonction pour mettre à jour une commune
def modify_commune(db: Session, id: int, updated_data: dict):
    """
    Met à jour une commune existante avec les nouvelles données fournies.
    
    :param db: Session de base de données
    :param id: Identifiant de la commune à mettre à jour
    :param updated_data: Données mises à jour sous forme de dictionnaire
    :return: La commune mise à jour, ou None si la commune n'existe pas
    """
    # Appelle la fonction du repository pour mettre à jour la commune
    return update_commune(db, id, updated_data)

# Fonction pour supprimer une commune
def remove_commune(db: Session, id: int):
    """
    Supprime une commune de la base de données par son identifiant (ID).
    
    :param db: Session de base de données
    :param id: Identifiant de la commune à supprimer
    :return: None
    """
    # Appelle la fonction du repository pour supprimer la commune
    return delete_commune(db, id)
