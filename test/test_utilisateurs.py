# Importation des modules nécessaires pour les tests
from fastapi.testclient import TestClient  # TestClient de FastAPI pour envoyer des requêtes HTTP à l'application
from src.main import app  # Importation de l'application FastAPI depuis le fichier principal
import pytest  # Importation de pytest pour la gestion des tests

# Initialisation du client de test, qui permet d'effectuer des requêtes à l'application FastAPI dans un environnement de test
client = TestClient(app)

# Test pour récupérer tous les utilisateurs
def test_get_all_utilisateurs():
    # Envoi d'une requête GET pour obtenir tous les utilisateurs
    response = client.get("/utilisateurs")
    
    # Vérification que la réponse a un statut HTTP 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Vérification que la réponse est une liste (devrait l'être si la route retourne tous les utilisateurs)
    assert isinstance(response.json(), list), "Response should be a list of utilisateurs"

# Test pour récupérer un utilisateur par son ID
def test_get_utilisateur_by_id():
    # Remplace "1" par un ID valide présent dans ta base de données pour ce test
    utilisateur_id = 5
    response = client.get(f"/utilisateurs/{utilisateur_id}")
    
    # Vérification que la réponse a un statut HTTP 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Vérification que la réponse est un dictionnaire représentant un utilisateur
    assert isinstance(response.json(), dict), "Response should be a dictionary representing an utilisateur"

# Test pour la création d'un nouvel utilisateur
# def test_create_utilisateur():
#     # Données à envoyer pour créer un nouvel utilisateur
#     data = {
#         "nom_utilisateur": "John",
#         "prenom_utilisateur": "Doe",
#         "username": "johndoe",  # Un username unique
#         # "couleur_fond_utilisateur": "blue",
#         "date_insc_utilisateur": "2025-01-06"  # Date d'inscription
#     }

#     # Envoi d'une requête POST pour créer un utilisateur avec les données fournies
#     response = client.post("/utilisateurs", json=data)
    
#     # Affichage du message d'erreur pour mieux comprendre le problème
#     print(response.json())  # Ajoutez cette ligne pour inspecter la réponse
    
#     # Vérification que la réponse a un statut HTTP 201 (Création réussie)
#     assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    
#     # Récupération du corps de la réponse au format JSON
#     response_json = response.json()
    
#     # Vérification que la réponse contient le champ 'username'
#     assert "username" in response_json, "Response should include a 'username' field"
    
#     # Vérification que le 'username' retourné correspond au 'username' envoyé dans la requête
#     assert response_json["username"] == data["username"], "Returned 'username' should match the input"

# Test pour la mise à jour d'un utilisateur
def test_update_utilisateur():
    utilisateur_id = 1  # Remplacer par un ID valide
    data = {
        "prenom_utilisateur": "Jane",
        "couleur_fond_utilisateur": "green"
    }

    # Envoi d'une requête PUT pour mettre à jour un utilisateur
    response = client.put(f"/utilisateurs/{utilisateur_id}", json=data)
    
    # Vérification que la réponse a un statut HTTP 200 (Mise à jour réussie)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Récupération du corps de la réponse au format JSON
    response_json = response.json()
    
    # Vérification que la mise à jour a bien été effectuée
    assert response_json["prenom_utilisateur"] == data["prenom_utilisateur"], "Updated 'prenom_utilisateur' should match the input"
    # assert response_json["couleur_fond_utilisateur"] == data["couleur_fond_utilisateur"], "Updated 'couleur_fond_utilisateur' should match the input"

# Test pour la suppression d'un utilisateur
# def test_delete_utilisateur():
#     utilisateur_id = 2  # Remplacer par un ID valide
    
#     # Envoi d'une requête DELETE pour supprimer un utilisateur
#     response = client.delete(f"/utilisateurs/{utilisateur_id}")
    
#     # Vérification que la réponse a un statut HTTP 200 (Suppression réussie)
#     assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
#     # Vérification que la réponse contient un message de succès
#     response_json = response.json()
#     assert response_json["detail"] == "Utilisateur supprimé avec succès", "Expected success message"

# # Test pour la gestion de l'utilisateur non trouvé lors de la récupération par ID
# def test_get_utilisateur_not_found():
#     utilisateur_id = 999  # ID qui n'existe pas dans la base de données
#     response = client.get(f"/utilisateurs/{utilisateur_id}")
    
#     # Vérification que la réponse a un statut HTTP 404 (Not Found)
#     assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    
#     # Vérification que la réponse contient un message d'erreur
#     response_json = response.json()
#     assert "detail" in response_json, "Response should contain a 'detail' field"
#     assert response_json["detail"] == "Utilisateur non trouvé", "Expected 'Utilisateur non trouvé' message"

# # Test pour la gestion de l'utilisateur non trouvé lors de la suppression
# def test_delete_utilisateur_not_found():
#     utilisateur_id = 999  # ID qui n'existe pas dans la base de données
#     response = client.delete(f"/utilisateurs/{utilisateur_id}")
    
#     # Vérification que la réponse a un statut HTTP 404 (Not Found)
#     assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    
#     # Vérification que la réponse contient un message d'erreur
#     response_json = response.json()
#     assert "detail" in response_json, "Response should contain a 'detail' field"
#     assert response_json["detail"] == "Utilisateur non trouvé", "Expected 'Utilisateur non trouvé' message"
