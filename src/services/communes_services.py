# services/commune.py
from sqlalchemy.orm import Session
from repositories.communes_repositories import (
    get_all_communes,
    get_commune_by_id,
    create_commune,
    update_commune,
    delete_commune
)

# Récupérer toutes les communes
def fetch_all_communes(db: Session):
    return get_all_communes(db)

# Récupérer une commune par son ID
def fetch_commune_by_id(db: Session, id: int):
    return get_commune_by_id(db, id)

# Créer une nouvelle commune
def add_commune(db: Session, commune_data: dict):
    return create_commune(db, commune_data)

# Mettre à jour une commune
def modify_commune(db: Session, id: int, updated_data: dict):
    return update_commune(db, id, updated_data)

# Supprimer une commune
def remove_commune(db: Session, id: int):
    return delete_commune(db, id)
