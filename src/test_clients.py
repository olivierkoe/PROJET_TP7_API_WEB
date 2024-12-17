# Importation des modules nécessaires pour les tests
from fastapi.testclient import TestClient  # TestClient de FastAPI pour envoyer des requêtes HTTP à l'application
from .main import app  # Importation de l'application FastAPI depuis le fichier principal
import pytest  # Importation de pytest pour la gestion des tests

# Initialisation du client de test, qui permet d'effectuer des requêtes à l'application FastAPI dans un environnement de test
client = TestClient(app)

# Test pour récupérer tous les clients
def test_get_all_clients():
    # Envoi d'une requête GET pour obtenir tous les clients
    response = client.get("/clients")
    
    # Vérification que la réponse a un statut HTTP 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Vérification que la réponse est une liste (devrait l'être si la route retourne tous les clients)
    assert isinstance(response.json(), list), "Response should be a list of clients"

# Test pour récupérer un client par son ID
def test_get_client_by_id():

    # Remplace "1" par un ID valide présent dans ta base de données pour ce test
    client_id = 5
    response = client.get(f"/clients/{client_id}")
    
    # Vérification que la réponse a un statut HTTP 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Vérification que la réponse est un dictionnaire représentant un client
    assert isinstance(response.json(), dict), "Response should be a dictionary representing a client"

# Test pour la création d'un nouveau client
def test_create_client():
    # Données à envoyer pour créer un nouveau client
    data = {

        "nomcli": "John Does",  # Nom du client
        "emailcli": "l9mEsj@example.com",  # Email du client

    }

    # Envoi d'une requête POST pour créer un client avec les données fournies
    response = client.post("/clients", json=data)
    
    # Vérification que la réponse a un statut HTTP 201 (Création réussie)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    
    # Récupération du corps de la réponse au format JSON
    response_json = response.json()
    
    # Vérification que la réponse contient le champ 'emailcli'
    assert "emailcli" in response_json, "Response should include an 'emailcli' field"
    
    # Vérification que le 'nomcli' retourné correspond au 'nomcli' envoyé dans la requête
    assert response_json["nomcli"] == data["nomcli"], "Returned 'nomcli' should match the input"
