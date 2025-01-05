from fastapi.testclient import TestClient
from fastapi import HTTPException, status
from src.main import app  # Assurez-vous d'avoir la bonne importation de votre application FastAPI
import pytest

# Initialisation du client de test
client = TestClient(app)

# Test pour récupérer tous les départements
def test_get_all_departements():
    response = client.get("/departements")
    
    # Vérification du statut de la réponse
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Vérification que la réponse est une liste de départements
    assert isinstance(response.json(), list), "Response should be a list of departments"

# Test pour récupérer un département par son code
def test_get_departement_by_id():
    code_dept = "75"  # Remplacez ce code par un code existant dans votre base de données
    response = client.get(f"/departements/{code_dept}")
    
    # Vérification du statut de la réponse
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Vérification que la réponse est un dictionnaire représentant un département
    assert isinstance(response.json(), dict), "Response should be a dictionary representing a department"

# Test pour la création d'un nouveau département
# def test_create_departement():
#     departement_data = {
#         "code_dept": "02",  # Code du département
#         "nom_dept": "Aisne",  # Nom du département
#     }

#     response = client.post("/departements", json=departement_data)

#     assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"

#     response_json = response.json()
#     assert response_json["code_dept"] == departement_data["code_dept"], "Returned 'code_dept' should match the input"
#     assert response_json["nom_dept"] == departement_data["nom_dept"], "Returned 'nom_dept' should match the input"

# Test pour la suppression d'un département inexistant
def test_delete_departement_not_found():
    code_dept = "999"  # Code inexistant
    response = client.delete(f"/departements/{code_dept}")
    
    # Vérification que la réponse retourne un code d'erreur 404
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    
    # Vérification que la réponse contient un message d'erreur
    assert "detail" in response.json(), "Response should contain an error message"
