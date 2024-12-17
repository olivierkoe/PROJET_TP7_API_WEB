from sqlalchemy.orm import Session
from models import Commande  # Importation du modèle Commande
from schemas.commande import CommandeCreate  # Importation du schéma CommandeCreate

# Fonction pour créer une nouvelle commande
def create_commande(db: Session, commande_data: CommandeCreate):
    # Conversion des données reçues (commande_data) en objet Commande
    commande = Commande(**commande_data.dict())
    
    # Ajout de la commande à la session de la base de données
    db.add(commande)
    
    # Validation des changements dans la base de données
    db.commit()
    
    # Rafraîchissement de l'objet pour charger les valeurs mises à jour (notamment l'ID)
    db.refresh(commande)
    
    # Retourne la commande nouvellement créée
    return commande

# Fonction pour récupérer toutes les commandes
def get_all_commandes(db: Session):
    # Requête pour récupérer toutes les commandes dans la base de données
    return db.query(Commande).all()

# Fonction pour récupérer une commande par son ID
def get_commande_by_id(db: Session, codcde: int):
    # Requête pour récupérer une commande en fonction de son identifiant (codcde)
    return db.query(Commande).filter(Commande.codcde == codcde).first()

# Fonction pour supprimer une commande
def delete_commande(db: Session, codcde: int):
    # Recherche de la commande à supprimer par son identifiant (codcde)
    commande = db.query(Commande).filter(Commande.codcde == codcde).first()
    
    # Si la commande existe, on la supprime
    if commande:
        db.delete(commande)  # Suppression de l'objet de la session
        db.commit()  # Validation de la suppression dans la base de données

# Fonction pour mettre à jour une commande
def update_commande(db: Session, codcde: int, updated_data: dict):
    # Recherche de la commande à mettre à jour par son identifiant (codcde)
    commande = db.query(Commande).filter(Commande.codcde == codcde).first()
    
    # Si la commande existe, on met à jour ses attributs
    if commande:
        for key, value in updated_data.items():
            # Si la commande a l'attribut à mettre à jour, on lui assigne la nouvelle valeur
            if hasattr(commande, key):
                setattr(commande, key, value)
        
        # Validation des changements dans la base de données
        db.commit()
        
        # Rafraîchissement de l'objet pour refléter les données mises à jour
        db.refresh(commande)
        
        # Retourne la commande mise à jour
        return commande
    
    # Si la commande n'existe pas, retourne None
    return None
