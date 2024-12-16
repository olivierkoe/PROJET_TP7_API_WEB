from pydantic import BaseModel

# Schéma pour la création d'un département
class DepartementCreate(BaseModel):
    code_dept: str
    nom_dept: str
    ordre_aff_dept: int

    class Config:
        from_attributes = True  # Utilisez "from_attributes" au lieu de "orm_mode"

# Schéma pour la réponse d'un département
class Departement(DepartementCreate):
    class Config:
        from_attributes = True  # Utilisez "from_attributes" au lieu de "orm_mode"
