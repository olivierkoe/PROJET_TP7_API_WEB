from sqlalchemy.orm import Session
from models import Departement

# Récupérer tous les départements
def get_all(db: Session):
    return db.query(Departement).all()

def get_by_id(db: Session, code_dept: str):
    return db.query(Departement).filter(Departement.code_dept == code_dept).first()

def create_departement(db: Session, departement_data: dict):
    new_departement = Departement(**departement_data)
    db.add(new_departement)
    db.commit()
    db.refresh(new_departement)
    return new_departement

def update_departement(db: Session, code_dept: str, updated_data: dict):
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()
    if not departement:
        raise ValueError(f"Département avec le code {code_dept} non trouvé")
    for key, value in updated_data.items():
        setattr(departement, key, value)
    db.commit()
    db.refresh(departement)
    return departement

def delete_departement(db: Session, code_dept: str):
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()
    if not departement:
        raise ValueError(f"Département avec le code {code_dept} non trouvé")
    db.delete(departement)
    db.commit()
