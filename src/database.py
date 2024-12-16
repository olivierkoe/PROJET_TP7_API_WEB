from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base

# Configuration de la base de données
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/fromagerie_com"

# Création de l'engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test de connexion et création de la base de données
try:
    # Vérification de la connexion à la base de données (par SQLAlchemy)
    with engine.connect() as connection:
        print("Connexion réussie à la base de données MySQL.")

    # Créer la base de données si elle n'existe pas (si vous souhaitez la créer via SQLAlchemy)
    # SQLAlchemy n'a pas de méthode directe pour créer une base de données, donc on utilise mysql.connector pour cela
    # Mais si la base de données est déjà créée, vous pouvez ignorer cette étape.
    with engine.connect() as connection:
        connection.execute("CREATE DATABASE IF NOT EXISTS fromagerie_com")
        connection.execute("USE fromagerie_com")
        # Créer toutes les tables dans la base de données en utilisant les classes de `models.py`
        Base.metadata.create_all(engine)
except Exception as e:
    print("Erreur de connexion :", e)


# Fonction pour récupérer une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
