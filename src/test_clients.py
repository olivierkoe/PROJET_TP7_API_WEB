from fastapi.testclient import TestClient
from main import app
import pytest

# Initialisation du client de test
client = TestClient(app)


def test_get_all_clients():
    response = client.get("/clients")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Response should be a list of clients"


def test_get_client_by_id():
    # Remplace "1" par un ID valide présent dans ta base de données pour ce test
    client_id = 4
    response = client.get(f"/clients/{client_id}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert isinstance(response.json(), dict), "Response should be a dictionary representing a client"


def test_create_client():
    # Données à envoyer pour créer un nouveau client
    data = {
        "nomcli": "John Does",
        "emailcli": "l9mEsj@example.com",
    }

    response = client.post("/clients", json=data)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    response_json = response.json()
    assert "emailcli" in response_json, "Response should include an 'emailcli' field"
    assert response_json["nomcli"] == data["nomcli"], "Returned 'nomcli' should match the input"