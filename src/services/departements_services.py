from sqlalchemy.orm import Session
from models import Departement  # Importation du modèle Departement

# Récupérer tous les départements
def get_all(db: Session):
    """
    Récupère tous les départements présents dans la base de données.
    
    :param db: Session de base de données
    :return: Liste des départements
    """
    # Effectue une requête pour récupérer tous les départements de la table Departement
    return db.query(Departement).all()

# Récupérer un département par son code
def get_by_id(db: Session, code_dept: str):
    """
    Récupère un département spécifique par son code.
    
    :param db: Session de base de données
    :param code_dept: Code du département à récupérer
    :return: Le département correspondant au code fourni, ou None si non trouvé
    """
    # Effectue une requête pour filtrer par le code du département et renvoie le premier résultat
    return db.query(Departement).filter(Departement.code_dept == code_dept).first()

# Créer un nouveau département
def create_departement(db: Session, departement_data: dict):
    """
    Crée un nouveau département dans la base de données avec les données fournies.
    
    :param db: Session de base de données
    :param departement_data: Données du département à créer sous forme de dictionnaire
    :return: Le département nouvellement créé
    """
    # Crée un nouvel objet Departement à partir des données fournies
    new_departement = Departement(**departement_data)
    
    # Ajoute le nouveau département à la session de base de données
    db.add(new_departement)
    
    # Effectue la transaction pour persister les données dans la base
    db.commit()
    
    # Rafraîchit l'objet pour récupérer les données actuelles après le commit (par exemple, les valeurs auto-générées comme l'ID)
    db.refresh(new_departement)
    
    # Renvoie le département créé
    return new_departement

# Mettre à jour un département
def update_departement(db: Session, code_dept: str, updated_data: dict):
    """
    Met à jour les informations d'un département existant en fonction de son code.
    
    :param db: Session de base de données
    :param code_dept: Code du département à mettre à jour
    :param updated_data: Données mises à jour sous forme de dictionnaire
    :return: Le département mis à jour
    :raises ValueError: Si le département avec le code donné n'est pas trouvé
    """
    # Recherche du département avec le code fourni
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()
    
    # Si le département n'existe pas, lever une exception
    if not departement:
        raise ValueError(f"Département avec le code {code_dept} non trouvé")
    
    # Mise à jour des attributs du département avec les nouvelles données
    for key, value in updated_data.items():
        setattr(departement, key, value)
    
    # Commit pour appliquer les changements dans la base de données
    db.commit()
    
    # Rafraîchissement de l'objet pour s'assurer que les données sont bien à jour
    db.refresh(departement)
    
    # Retourne le département mis à jour
    return departement

# Supprimer un département
def delete_departement(db: Session, code_dept: str):
    """
    Supprime un département de la base de données en fonction de son code.
    
    :param db: Session de base de données
    :param code_dept: Code du département à supprimer
    :raises ValueError: Si le département avec le code donné n'est pas trouvé
    """
    # Recherche du département avec le code fourni
    departement = db.query(Departement).filter(Departement.code_dept == code_dept).first()
    
    # Si le département n'existe pas, lever une exception
    if not departement:
        raise ValueError(f"Département avec le code {code_dept} non trouvé")
    
    # Suppression du département de la session de base de données
    db.delete(departement)
    
    # Commit pour appliquer la suppression dans la base de données
    db.commit()
