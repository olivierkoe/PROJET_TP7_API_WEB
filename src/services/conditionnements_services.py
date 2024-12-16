# services/conditionnement.py
from sqlalchemy.orm import Session
from repositories.conditionnements_repository import (
    get_all_conditionnements,
    get_conditionnement_by_id,
    create_conditionnement,
    update_conditionnement,
    delete_conditionnement
)

# Récupérer tous les conditionnements
def fetch_all_conditionnements(db: Session):
    return get_all_conditionnements(db)

# Récupérer un conditionnement par son ID
def fetch_conditionnement_by_id(db: Session, idcondit: int):
    return get_conditionnement_by_id(db, idcondit)

# Créer un nouveau conditionnement
def add_conditionnement(db: Session, conditionnement_data: dict):
    return create_conditionnement(db, conditionnement_data)

# Mettre à jour un conditionnement
def modify_conditionnement(db: Session, idcondit: int, updated_data: dict):
    return update_conditionnement(db, idcondit, updated_data)

# Supprimer un conditionnement
def remove_conditionnement(db: Session, idcondit: int):
    return delete_conditionnement(db, idcondit)
