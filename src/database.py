import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Assurez-vous que les modèles sont définis ici
from urllib.parse import quote_plus

# URL de connexion pour SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:@localhost/fromagerie_com"

# Création de l'engine SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Création de la session SQLAlchemy
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Fonction pour tester la connexion
def test_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="fromagerie_com",
            collation="utf8mb4_general_ci"
        )
        print("Connexion réussie à la base de données MySQL.")
        conn.close()  # Fermer la connexion après le test
    except mysql.connector.Error as err:
        print(f"Erreur de connexion : {err}")

# Test de connexion
test_connection()

# Créer les tables avec SQLAlchemy
Base.metadata.create_all(bind=engine)
