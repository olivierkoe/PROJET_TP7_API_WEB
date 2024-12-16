# schemas/commune.py
from pydantic import BaseModel

# Schéma pour la création d'une commune
class CommuneCreate(BaseModel):
    dep: str
    cp: str
    ville: str

    class Config:
        orm_mode = True  # Permet de lire directement les objets SQLAlchemy

# Schéma pour la réponse d'une commune
class Commune(CommuneCreate):
    id: int

    class Config:
        orm_mode = True
