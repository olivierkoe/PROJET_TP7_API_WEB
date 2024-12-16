# repositories/commune.py
from sqlalchemy.orm import Session
from models import Commune

# Fonction pour obtenir toutes les communes
def get_all_communes(db: Session):
    return db.query(Commune).all()

# Fonction pour obtenir une commune par son ID
def get_commune_by_id(db: Session, id: int):
    return db.query(Commune).filter(Commune.id == id).first()

# Fonction pour créer une nouvelle commune
def create_commune(db: Session, commune_data: dict):
    commune = Commune(**commune_data)
    db.add(commune)
    db.commit()
    db.refresh(commune)
    return commune

# Fonction pour mettre à jour une commune
def update_commune(db: Session, id: int, updated_data: dict):
    commune = db.query(Commune).filter(Commune.id == id).first()
    if not commune:
        return None
    for key, value in updated_data.items():
        if hasattr(commune, key):
            setattr(commune, key, value)
    db.commit()
    db.refresh(commune)
    return commune

# Fonction pour supprimer une commune
def delete_commune(db: Session, id: int):
    commune = db.query(Commune).filter(Commune.id == id).first()
    if commune:
        db.delete(commune)
        db.commit()
    return commune
