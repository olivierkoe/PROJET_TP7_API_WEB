# repositories/commandes_repositories.py
from sqlalchemy.orm import Session
from models import Commande

# Créer une commande
def create_commande(db: Session, commande_data: dict):
    commande = Commande(**commande_data)
    db.add(commande)
    db.commit()
    db.refresh(commande)
    return commande

# Récupérer une commande par son ID
def get_commande_by_id(db: Session, codcde: int):
    return db.query(Commande).filter(Commande.codcde == codcde).first()

# Récupérer toutes les commandes
def get_all_commandes(db: Session):
    return db.query(Commande).all()

# Supprimer une commande
def delete_commande(db: Session, codcde: int):
    commande = db.query(Commande).filter(Commande.codcde == codcde).first()
    if commande:
        db.delete(commande)
        db.commit()

# Mettre à jour une commande
def update_commande(db: Session, codcde: int, updated_data: dict):
    commande = db.query(Commande).filter(Commande.codcde == codcde).first()
    if commande:
        for key, value in updated_data.items():
            if hasattr(commande, key):
                setattr(commande, key, value)
        db.commit()
        db.refresh(commande)
        return commande
    return None
