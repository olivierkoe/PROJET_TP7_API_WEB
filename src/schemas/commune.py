from pydantic import BaseModel, ConfigDict

# Schéma pour la création d'une commune
class CommuneCreate(BaseModel):
    dep: str
    cp: str
    ville: str

    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'une commune
class Commune(CommuneCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
