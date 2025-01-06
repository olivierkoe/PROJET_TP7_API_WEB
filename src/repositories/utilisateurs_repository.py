from src.models import Utilisateur  # Importation du modèle utilisateur depuis le module models
from sqlalchemy.orm import Session  # Importation de la classe Session pour interagir avec la base de données
from datetime import date
from fastapi import HTTPException, status

def get_all_utilisateurs(db: Session):
    """
    Récupère tous les utilisateurs depuis la base de données.
    :param db: Session de base de données
    :return: Liste de tous les utilisateurs
    """
    return list(db.query(Utilisateur).all())  # Exécution de la requête pour récupérer tous les utilisateurs


def get_utilisateur_by_id(db: Session, id: int):
    """
    Récupère un utilisateur en fonction de son ID.
    :param db: Session de base de données
    :param id: Identifiant du utilisateur
    :return: utilisateur correspondant à l'ID
    :raises ValueError: Si le utilisateur n'est pas trouvé
    :raises RuntimeError: Si une erreur se produit pendant la récupération
    """
    try:
        utilisateur = db.get(Utilisateur, id)  # Récupère le utilisateur par ID
        if not utilisateur:  # Si aucun utilisateur n'est trouvé
            raise ValueError(f"utilisateur avec ID {id} introuvable.")  # Lève une exception si non trouvé
        return utilisateur  # Retourne le utilisateur trouvé
    except Exception as e:
        # En cas d'erreur, lève une exception RuntimeError
        raise RuntimeError(f"Erreur lors de la récupération du utilisateur: {str(e)}")


def create_utilisateur(db: Session, utilisateur_data: dict):
    """
    Crée un nouvel utilisateur dans la base de données.
    Vérifie si le `username` existe déjà avant de procéder à la création.
    
    :param db: Session de base de données
    :param utilisateur_data: Dictionnaire des données de l'utilisateur (par exemple, nom, prénom, username)
    :return: L'utilisateur nouvellement créé
    :raises HTTPException: Si le `username` existe déjà ou en cas d'autres erreurs
    """
    try:
        # Vérifie si un utilisateur avec le même username existe déjà
        existing_user = db.query(Utilisateur).filter(Utilisateur.username == utilisateur_data.get("username")).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"L'utilisateur avec le username '{utilisateur_data['username']}' existe déjà."
            )

        # Ajoute une date d'inscription par défaut si elle n'est pas fournie
        if not utilisateur_data.get("date_insc_utilisateur"):
            utilisateur_data["date_insc_utilisateur"] = date.today()

        # Crée un nouvel utilisateur avec les données fournies
        new_utilisateur = Utilisateur(**utilisateur_data)
        db.add(new_utilisateur)  # Ajoute l'utilisateur à la session
        db.commit()  # Effectue la transaction
        db.refresh(new_utilisateur)  # Rafraîchit l'objet pour obtenir l'état mis à jour

        return new_utilisateur  # Retourne l'utilisateur créé
    except HTTPException:
        raise  # Relève l'exception pour la gérer plus haut
    except Exception as e:
        db.rollback()  # Annule la transaction en cas d'erreur
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la création de l'utilisateur : {str(e)}"
        )




def update_utilisateur(db: Session, utilisateur_id: int, utilisateur_data: dict):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == utilisateur_id).first()
    
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    for key, value in utilisateur_data.items():
        setattr(utilisateur, key, value)
    
    try:
        db.commit()  # Effectuer la mise à jour
        db.refresh(utilisateur)  # Rafraîchir les données de l'instance
    except Exception as e:
        db.rollback()  # Annuler en cas d'erreur
        raise HTTPException(status_code=500, detail=f"Erreur lors de la mise à jour du utilisateur: {str(e)}")
    return utilisateur
def delete_utilisateur(db: Session, utilisateur_id: int):
    """
    Supprime un utilisateur de la base de données.
    :param db: Session de base de données
    :param utilisateur_id: ID de l'utilisateur à supprimer
    :raises HTTPException: Si l'utilisateur n'existe pas
    """
    # Chercher l'utilisateur dans la base de données
    utilisateur = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == utilisateur_id).first()

    # Vérifier si l'utilisateur existe
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    # Essayer de supprimer l'utilisateur
    try:
        db.delete(utilisateur)  # Supprime l'utilisateur
        db.commit()  # Valide la transaction
    except Exception as e:
        db.rollback()  # Annule la transaction en cas d'erreur
        raise HTTPException(status_code=500, detail=f"Erreur lors de la suppression du utilisateur: {str(e)}")

    return {"detail": "Utilisateur supprimé avec succès"}