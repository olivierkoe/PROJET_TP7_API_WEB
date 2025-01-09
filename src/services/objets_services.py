# services/objets_service.py
from sqlalchemy.orm import Session
from src.models import Objet  # Importation du modèle Objet
from src.schemas.objet import ObjetCreate  # Importation du schéma ObjetCreate

# Fonction pour créer un nouvel objet
def create_objet(db: Session, objet_data: ObjetCreate):
    """
    Crée un nouvel objet dans la base de données.
    :param db: Session de base de données
    :param objet_data: Données de l'objet à créer
    :return: L'objet créé
    """
    # Crée une nouvelle instance de l'objet sans inclure le champ `codobj` (auto-incrémenté par la base)
    new_objet = Objet(
        libobj=objet_data.libobj,
        tailleobj=objet_data.tailleobj,
        puobj=objet_data.puobj,
        poidsobj=objet_data.poidsobj,
        indispobj=objet_data.indispobj,
        o_imp=objet_data.o_imp,
        o_aff=objet_data.o_aff,
        o_cartp=objet_data.o_cartp,
        points=objet_data.points,
        o_ordre_aff=objet_data.o_ordre_aff
    )
    
    # Ajouter l'objet à la session de la base de données
    db.add(new_objet)
    
    try:
        # Commit la transaction pour enregistrer l'objet dans la base de données
        db.commit()
        db.refresh(new_objet)  # Rafraîchit l'objet pour récupérer l'ID auto-incrémenté
        return new_objet
    except Exception as e:
        db.rollback()  # Annule la transaction en cas d'erreur
        raise e  # Gérer l'exception selon les besoins de votre application


# Fonction pour récupérer tous les objets
def get_all_objets(db: Session):
    """
    Récupère tous les objets dans la base de données.
    :param db: Session de base de données
    :return: Liste de tous les objets
    """
    # Requête pour récupérer tous les objets dans la base de données
    return db.query(Objet).all()

# Fonction pour récupérer un objet par son ID
def get_objet_by_id(db: Session, codobj: int):
    """
    Récupère un objet par son ID.
    :param db: Session de base de données
    :param codobj: Identifiant de l'objet à récupérer
    :return: L'objet correspondant ou None si l'objet n'existe pas
    """
    # Requête pour récupérer un objet en fonction de son identifiant (codobj)
    return db.query(Objet).filter(Objet.codobj == codobj).first()

# Fonction pour supprimer un objet
def delete_objet(db: Session, codobj: int):
    """
    Supprime un objet en fonction de son ID.
    :param db: Session de base de données
    :param codobj: Identifiant de l'objet à supprimer
    """
    # Recherche de l'objet à supprimer par son identifiant (codobj)
    objet = db.query(Objet).filter(Objet.codobj == codobj).first()
    
    # Si l'objet existe, on le supprime
    if objet:
        db.delete(objet)  # Suppression de l'objet de la session
        db.commit()  # Validation de la suppression dans la base de données

# Fonction pour mettre à jour un objet
def update_objet(db: Session, codobj: int, updated_data: dict):
    """
    Met à jour un objet en fonction de son ID et des nouvelles données.
    :param db: Session de base de données
    :param codobj: Identifiant de l'objet à mettre à jour
    :param updated_data: Données mises à jour sous forme de dictionnaire
    :return: L'objet mis à jour ou None si l'objet n'existe pas
    """
    # Recherche de l'objet à mettre à jour par son identifiant (codobj)
    objet = db.query(Objet).filter(Objet.codobj == codobj).first()
    
    # Si l'objet existe, on met à jour ses attributs
    if objet:
        # Si updated_data est une instance de ObjetCreate, convertir en dictionnaire
        if isinstance(updated_data, ObjetCreate):
            updated_data = updated_data.dict()

        # Itérer sur les données mises à jour (sous forme de dictionnaire)
        for key, value in updated_data.items():
            # Si l'objet a l'attribut à mettre à jour, on lui assigne la nouvelle valeur
            if hasattr(objet, key):
                setattr(objet, key, value)
        
        # Validation des changements dans la base de données
        try:
            db.commit()
            db.refresh(objet)  # Rafraîchissement de l'objet pour refléter les modifications
        except Exception as e:
            db.rollback()  # Annule la transaction si une erreur se produit
            raise e  # Vous pouvez gérer cette exception en fonction de votre logique (par exemple, envoyer une réponse d'erreur)
        
        # Retourne l'objet mis à jour
        return objet
    
    # Si l'objet n'existe pas, retourne None
    return None


