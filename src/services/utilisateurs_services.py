from src.repositories.utilisateurs_repository import (
    get_all_utilisateurs,           # Fonction pour récupérer tous les utilisateurs
    get_utilisateur_by_id,          # Fonction pour récupérer un utilisateur par son identifiant
    create_utilisateur as repo_create_utilisateur,  # Fonction pour créer un nouveau utilisateur
    update_utilisateur as repo_update_utilisateur,  # Fonction pour mettre à jour un utilisateur existant
    delete_utilisateur as repo_delete_utilisateur   # Fonction pour supprimer un utilisateur
)

# Fonction pour récupérer tous les utilisateurs
def get_all(db):
    try:
        # Appel à la fonction du dépôt pour récupérer tous les utilisateurs
        return get_all_utilisateurs(db)
    except Exception as e:
        # En cas d'erreur, une RuntimeError est levée
        raise RuntimeError(f"Erreur lors de la récupération des utilisateurs : {str(e)}")

# Fonction pour récupérer un utilisateur par son ID
def get_by_id(db, id):
    try:
        # Appel à la fonction du dépôt pour récupérer un utilisateur par son identifiant
        return get_utilisateur_by_id(db, id)
    except Exception as e:
        # En cas d'erreur ou de utilisateur non trouvé, une ValueError est levée
        raise ValueError(f"utilisateur avec ID {id} introuvable : {str(e)}")

# Fonction pour créer un nouveau utilisateur
def create_utilisateur(db, utilisateur_data):
    try:
        # Appel à la fonction du dépôt pour créer un utilisateur avec les données fournies
        return repo_create_utilisateur(db, utilisateur_data)
    except Exception as e:
        # En cas d'erreur, une RuntimeError est levée
        raise RuntimeError(f"Erreur lors de la création du utilisateur : {str(e)}")

# Fonction pour mettre à jour les informations d'un utilisateur
def update_utilisateur(db, id, updated_data):
    """
    Met à jour les informations d'un utilisateur.
    :param db: Session de base de données
    :param id: Identifiant du utilisateur à mettre à jour
    :param updated_data: Données mises à jour (dictionnaire)
    :return: utilisateur mis à jour
    """
    try:
        # Appel à la fonction du dépôt pour mettre à jour un utilisateur avec les données mises à jour
        return repo_update_utilisateur(db, id, updated_data)
    except ValueError as ve:
        # Si le utilisateur n'existe pas (id non trouvé), une ValueError est levée
        raise ValueError(f"utilisateur avec ID {id} introuvable : {str(ve)}")
    except Exception as e:
        # En cas d'erreur, une RuntimeError est levée
        raise RuntimeError(f"Erreur lors de la mise à jour du utilisateur : {str(e)}")

# Fonction pour supprimer un utilisateur
def delete_utilisateur(db, id):
    try:
        # Appel à la fonction du dépôt pour supprimer un utilisateur par son identifiant
        return repo_delete_utilisateur(db, id)
    except Exception as e:
        # En cas d'erreur, une RuntimeError est levée
        raise RuntimeError(f"Erreur lors de la suppression du utilisateur : {str(e)}")
