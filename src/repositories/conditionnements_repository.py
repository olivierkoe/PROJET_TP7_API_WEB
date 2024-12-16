from sqlalchemy.orm import Session
from models import Conditionnement

# Fonction pour obtenir tous les conditionnements
def get_all_conditionnements(db: Session):
    return db.query(Conditionnement).all()

# Fonction pour obtenir un conditionnement par son ID
def get_conditionnement_by_id(db: Session, idcondit: int):
    return db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()

# Fonction pour créer un nouveau conditionnement
def create_conditionnement(db: Session, conditionnement_data: dict):
    conditionnement = Conditionnement(**conditionnement_data)
    db.add(conditionnement)
    db.commit()
    db.refresh(conditionnement)
    return conditionnement

# Fonction pour mettre à jour un conditionnement
def update_conditionnement(db: Session, idcondit: int, updated_data: dict):
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()
    if not conditionnement:
        return None
    for key, value in updated_data.items():
        if hasattr(conditionnement, key):
            setattr(conditionnement, key, value)
    db.commit()
    db.refresh(conditionnement)
    return conditionnement

# Fonction pour supprimer un conditionnement
def delete_conditionnement(db: Session, idcondit: int):
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()
    if conditionnement:
        db.delete(conditionnement)
        db.commit()
    return conditionnement
