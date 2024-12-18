from src.models import Client  # Importation du modèle Client depuis le module models
from sqlalchemy.orm import Session  # Importation de la classe Session pour interagir avec la base de données


def get_all_clients(db: Session):
    """
    Récupère tous les clients depuis la base de données.
    :param db: Session de base de données
    :return: Liste de tous les clients
    """
    return list(db.query(Client).all())  # Exécution de la requête pour récupérer tous les clients


def get_client_by_id(db: Session, id: int):
    """
    Récupère un client en fonction de son ID.
    :param db: Session de base de données
    :param id: Identifiant du client
    :return: Client correspondant à l'ID
    :raises ValueError: Si le client n'est pas trouvé
    :raises RuntimeError: Si une erreur se produit pendant la récupération
    """
    try:
        client = db.get(Client, id)  # Récupère le client par ID
        if not client:  # Si aucun client n'est trouvé
            raise ValueError(f"Client avec ID {id} introuvable.")  # Lève une exception si non trouvé
        return client  # Retourne le client trouvé
    except Exception as e:
        # En cas d'erreur, lève une exception RuntimeError
        raise RuntimeError(f"Erreur lors de la récupération du client: {str(e)}")


def create_client(db: Session, client_data: dict):
    """
    Crée un nouveau client dans la base de données.
    :param db: Session de base de données
    :param client_data: Dictionnaire des données du client (par exemple, nom, adresse)
    :return: Le client nouvellement créé
    :raises RuntimeError: Si une erreur se produit pendant la création
    """
    try:
        new_client = Client(**client_data)  # Crée un nouveau client avec les données fournies
        db.add(new_client)  # Ajoute le client à la session
        db.commit()  # Effectue la transaction
        db.refresh(new_client)  # Rafraîchit l'objet pour obtenir l'état mis à jour
        return new_client  # Retourne le client créé
    except Exception as e:
        db.rollback()  # Annule la transaction en cas d'erreur
        raise RuntimeError(f"Erreur lors de la création du client: {str(e)}")


def update_client(db: Session, id: int, updated_data: dict):
    """
    Met à jour un client en fonction de son ID et des nouvelles données.
    :param db: Session de base de données
    :param id: Identifiant du client
    :param updated_data: Données mises à jour (dictionnaire)
    :return: Client mis à jour
    :raises ValueError: Si le client avec l'ID donné n'existe pas
    """
    client = db.query(Client).filter(Client.codcli == id).first()  # Recherche du client par ID
    if not client:  # Si le client n'existe pas
        raise ValueError(f"Client avec ID {id} introuvable.")  # Lève une exception si non trouvé
    
    # Mise à jour des données du client
    for key, value in updated_data.items():  # Parcours des nouvelles données
        if hasattr(client, key):  # Vérifie si le client possède cet attribut
            setattr(client, key, value)  # Met à jour l'attribut
    
    db.commit()  # Effectue la transaction pour sauvegarder les changements
    db.refresh(client)  # Rafraîchit l'objet pour obtenir l'état mis à jour
    return client  # Retourne le client mis à jour


def delete_client(db: Session, codcli: int):
    """
    Supprime un client en fonction de son code client.
    :param db: Session de base de données
    :param codcli: Code du client à supprimer
    :return: Message de confirmation de la suppression
    :raises ValueError: Si le client avec le code spécifié n'est pas trouvé
    :raises RuntimeError: Si une erreur se produit pendant la suppression
    """
    client = db.query(Client).filter(Client.codcli == codcli).first()  # Recherche du client par code
    if not client:  # Si le client n'existe pas
        raise ValueError(f"Client avec le code {codcli} introuvable.")  # Lève une exception si non trouvé
    try:
        db.delete(client)  # Supprime le client de la session
        db.commit()  # Effectue la transaction pour supprimer le client de la base de données
    except Exception as e:
        db.rollback()  # Annule la transaction en cas d'erreur
        raise RuntimeError(f"Erreur lors de la suppression du client : {str(e)}")  # Lève une exception si une erreur se produit
    return {"message": f"Client avec le code {codcli} supprimé avec succès."}  # Retourne un message de confirmation
