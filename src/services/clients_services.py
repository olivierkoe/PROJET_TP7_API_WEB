from src.repositories.clients_repository import (
    get_all_clients,           # Fonction pour récupérer tous les clients
    get_client_by_id,          # Fonction pour récupérer un client par son identifiant
    create_client as repo_create_client,  # Fonction pour créer un nouveau client
    update_client as repo_update_client,  # Fonction pour mettre à jour un client existant
    delete_client as repo_delete_client   # Fonction pour supprimer un client
)

# Fonction pour récupérer tous les clients
def get_all(db):
    try:
        # Appel à la fonction du dépôt pour récupérer tous les clients
        return get_all_clients(db)
    except Exception as e:
        # En cas d'erreur, une RuntimeError est levée
        raise RuntimeError(f"Erreur lors de la récupération des clients : {str(e)}")

# Fonction pour récupérer un client par son ID
def get_by_id(db, id):
    try:
        # Appel à la fonction du dépôt pour récupérer un client par son identifiant
        return get_client_by_id(db, id)
    except Exception as e:
        # En cas d'erreur ou de client non trouvé, une ValueError est levée
        raise ValueError(f"Client avec ID {id} introuvable : {str(e)}")

# Fonction pour créer un nouveau client
def create_client(db, client_data):
    try:
        # Appel à la fonction du dépôt pour créer un client avec les données fournies
        return repo_create_client(db, client_data)
    except Exception as e:
        # En cas d'erreur, une RuntimeError est levée
        raise RuntimeError(f"Erreur lors de la création du client : {str(e)}")

# Fonction pour mettre à jour les informations d'un client
def update_client(db, id, updated_data):
    """
    Met à jour les informations d'un client.
    :param db: Session de base de données
    :param id: Identifiant du client à mettre à jour
    :param updated_data: Données mises à jour (dictionnaire)
    :return: Client mis à jour
    """
    try:
        # Appel à la fonction du dépôt pour mettre à jour un client avec les données mises à jour
        return repo_update_client(db, id, updated_data)
    except ValueError as ve:
        # Si le client n'existe pas (id non trouvé), une ValueError est levée
        raise ValueError(f"Client avec ID {id} introuvable : {str(ve)}")
    except Exception as e:
        # En cas d'erreur, une RuntimeError est levée
        raise RuntimeError(f"Erreur lors de la mise à jour du client : {str(e)}")

# Fonction pour supprimer un client
def delete_client(db, id):
    try:
        # Appel à la fonction du dépôt pour supprimer un client par son identifiant
        return repo_delete_client(db, id)
    except Exception as e:
        # En cas d'erreur, une RuntimeError est levée
        raise RuntimeError(f"Erreur lors de la suppression du client : {str(e)}")
