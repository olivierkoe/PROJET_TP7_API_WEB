from sqlalchemy.orm import Session
from models import Departement

def get_all_departements(db: Session):
    return db.query(Departement).all()

def get_departement_by_id(db: Session, code_dept: str):
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()
    if not departement:
        raise ValueError(f"Département avec le code '{code_dept}' introuvable.")
    return departement

def create_departement(db: Session, departement_data: DepartementCreate):
    print(f"Received departement data: {departement_data}")
    departement_dict = departement_data.dict()
    print(f"Converted to dict: {departement_dict}")
    
    departement = Departement(**departement_dict)
    db.add(departement)
    db.commit()
    db.refresh(departement)
    return departement


def delete_departement(db: Session, code_dept: str):
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()
    if not departement:
        raise ValueError(f"Département avec le code '{code_dept}' introuvable.")
    db.delete(departement)
    db.commit()

def update_departement(db: Session, code_dept: str, updated_data: dict):
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()
    if not departement:
        raise ValueError(f"Département avec le code '{code_dept}' introuvable.")
    
    for key, value in updated_data.items():
        if hasattr(departement, key):
            setattr(departement, key, value)
    
    db.commit()
    db.refresh(departement)
    return departement
