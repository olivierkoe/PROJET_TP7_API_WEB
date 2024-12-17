from pydantic import BaseModel, ConfigDict

# Schéma pour la création d'un département
class DepartementCreate(BaseModel):
    code_dept: str
    nom_dept: str
    # ordre_aff_dept: int

    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'un département
class Departement(DepartementCreate):

    model_config = ConfigDict(from_attributes=True)
