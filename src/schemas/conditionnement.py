from pydantic import BaseModel, ConfigDict
from decimal import Decimal

# Schéma pour créer un conditionnement
class ConditionnementCreate(BaseModel):
    libcondit: str
    poidscondit: int
    # prixcond: Decimal
    ordreimp: int

    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'un conditionnement
class Conditionnement(ConditionnementCreate):
    idcondit: int

    model_config = ConfigDict(from_attributes=True)
