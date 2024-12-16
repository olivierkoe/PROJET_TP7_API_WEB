from models import Client
from sqlalchemy.orm import Session


def get_all_clients(db: Session):
    return list(db.query(Client).all())

def get_client_by_id(db: Session, id: int):
    try:
        client = db.get(Client, id)
        if not client:
            raise ValueError(f"Client avec ID {id} introuvable.")
        return client
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la récupération du client: {str(e)}")

def create_client(db: Session, client_data: dict):
    try:
        new_client = Client(**client_data)  # Assurez-vous que le dictionnaire correspond au modèle SQLAlchemy
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client
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
    """
    client = db.query(Client).filter(Client.codcli == id).first()
    if not client:
        raise ValueError(f"Client avec ID {id} introuvable.")
    
    for key, value in updated_data.items():
        if hasattr(client, key):
            setattr(client, key, value)

    db.commit()
    db.refresh(client)
    return client

def delete_client(db: Session, codcli: int):
    # Recherche du client par son code
    client = db.query(Client).filter(Client.codcli == codcli).first()
    if not client:
        raise ValueError(f"Client avec le code {codcli} introuvable.")
    try:
        db.delete(client)  # Suppression du client
        db.commit()        # Validation des changements
    except Exception as e:
        db.rollback()      # Annulation des changements en cas d'erreur
        raise RuntimeError(f"Erreur lors de la suppression du client : {str(e)}")
    return {"message": f"Client avec le code {codcli} supprimé avec succès."}