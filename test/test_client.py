from fastapi.testclient import TestClient
from src.main import app
from src.database import SessionLocal
from src.models import Client, Commune  # Importer correctement les modèles

client = TestClient(app)

# Fonction pour créer une ville de test
def create_test_city(db):
    city = Commune(dep="75", cp="75001", ville="Test City")  # Exemple de ville
    db.add(city)
    db.commit()
    db.refresh(city)
    return city

# Fonction pour créer un client de test
def create_test_client(db, city):
    client = Client(
        genrecli="M",
        nomcli="Client Test",
        prenomcli="Test",
        adresse1cli="123 Test Street",
        emailcli="clienttest@example.com",
        telcli="0123456789",
        portcli="0987654321",
        newsletter=True,
        villecli_id=city.id  # Associer à une ville existante
    )
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

# Test pour récupérer tous les clients
def test_get_all_clients():
    response = client.get("/client/")  # Assurez-vous que l'endpoint est correct
    assert response.status_code == 200  # Vérifie que la réponse est OK (200)
    assert isinstance(response.json(), list)  # Vérifie que la réponse est une liste

# Test pour récupérer un client par ID
def test_get_client_by_id():
    # Créer une session de base de données pour le test
    db = SessionLocal()
    
    # Créer une ville de test
    test_city = create_test_city(db)
    
    # Créer un client de test
    test_client = create_test_client(db, test_city)
    
    # Récupérer le client par son ID
    response = client.get(f"/client/{test_client.codcli}")  # Remplacez avec l'URL correcte
    assert response.status_code == 200  # Vérifie que la réponse est OK (200)
    assert "codcli" in response.json()  # Vérifie que l'ID du client est présent dans la réponse
    assert response.json()["nomcli"] == test_client.nomcli  # Vérifie que le nom du client correspond
    db.close()  # Fermer la session de la base de données après test

# Test pour créer un client
def test_create_client():
    # Créer une session de base de données pour le test
    db = SessionLocal()
    
    # Créer une ville de test
    test_city = create_test_city(db)
    
    # Données du client à ajouter
    client_data = {
        "genrecli": "M",
        "nomcli": "Client Test",
        "prenomcli": "Test",
        "adresse1cli": "123 Test Street",
        "emailcli": "clienttest@example.com",
        "telcli": "0123456789",
        "portcli": "0987654321",
        "newsletter": True,
        "villecli_id": test_city.id  # ID de la ville créée
    }
    
    # Envoyer une requête POST pour créer le client
    response = client.post("/client/", json=client_data)  # Assurez-vous que l'endpoint est correct
    assert response.status_code == 201  # Vérifie que la réponse est OK (201 créé)
    assert response.json()["nomcli"] == client_data["nomcli"]  # Vérifie que le nom du client correspond
    assert response.json()["emailcli"] == client_data["emailcli"]  # Vérifie que l'email du client correspond
    assert response.json()["villecli_id"] == client_data["villecli_id"]  # Vérifie que la ville est correctement assignée
    db.close()  # Fermer la session de la base de données après test
