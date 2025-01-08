# Importation des modules nécessaires
from fastapi import FastAPI  # Importation de la classe FastAPI pour créer l'application
from src.router.clients_router import router_client  # Importation du router des clients
from src.router.departements_router import router_departement  # Importation du router des départements
from src.router.conditionnements_router import router_conditionnement  # Importation du router des conditionnements
from src.router.commandes_router import router_commande  # Importation du router des commandes
from src.router.communes_router import router_commune  # Importation du router des communes
from src.router.utilisateurs_router import router_utilisateur  # Importation du router des utilisateurs
from src.database import engine  # Importation de l'engine de la base de données (connexion à la BDD)
from src.models import Base  # Importation de la classe Base pour la création des tables


# Création de l'application FastAPI
app = FastAPI()

# Inclusion des routers dans l'application FastAPI
# Chaque routeur correspond à un domaine spécifique (clients, départements, conditionnements, etc.)

app.include_router(router_client, prefix="/clients", tags=["Clients"])  # Routes pour la gestion des clients
app.include_router(router_departement, prefix="/departements", tags=["Départements"])  # Routes pour la gestion des départements
app.include_router(router_conditionnement, prefix="/conditionnements", tags=["Conditionnements"])  # Routes pour la gestion des conditionnements
app.include_router(router_commune, prefix="/communes", tags=["Communes"])  # Routes pour la gestion des communes
app.include_router(router_commande, prefix="/commandes", tags=["Commandes"])  # Routes pour la gestion des commandes
app.include_router(router_utilisateur, prefix="/utilisateurs", tags=["Utilisateurs"])  # Routes pour la gestion des utilisateurs

# Commande pour créer toutes les tables définies dans les modèles (models.py) si elles n'existent pas déjà dans la base de données.
# Cette commande est exécutée lors du démarrage de l'application pour s'assurer que la structure de la base est à jour.
Base.metadata.create_all(engine)
