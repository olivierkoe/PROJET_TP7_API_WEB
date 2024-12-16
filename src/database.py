from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration de la base de données
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/fromagerie_com"

# Création de l'engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de données pour les modèles
Base = declarative_base()

# Fonction pour récupérer une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
