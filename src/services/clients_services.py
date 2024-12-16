from repositories.clients_repository import get_all_clients, get_client_by_id, create_client as repo_create_client, delete_client as repo_delete_client

def get_all(db):
    try:
        return get_all_clients(db)
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la récupération des clients : {str(e)}")

def get_by_id(db, id):
    try:
        return get_client_by_id(db, id)
    except Exception as e:
        raise ValueError(f"Client avec ID {id} introuvable : {str(e)}")

def create_client(db, client_data):
    try:
        return repo_create_client(db, client_data)
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la création du client : {str(e)}")

def delete_client(db, id):
    try:
        return repo_delete_client(db, id)
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la suppression du client : {str(e)}")
