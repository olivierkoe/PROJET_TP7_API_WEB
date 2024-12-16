# schemas/conditionnement.py
from pydantic import BaseModel
from decimal import Decimal

# Schéma pour créer un conditionnement
class ConditionnementCreate(BaseModel):
    libcondit: str
    poidscondit: int
    # prixcond: Decimal
    ordreimp: int

    class Config:
        orm_mode = True  # Permet de lire directement les objets SQLAlchemy

# Schéma pour la réponse d'un conditionnement
class Conditionnement(ConditionnementCreate):
    idcondit: int

    class Config:
        orm_mode = True
