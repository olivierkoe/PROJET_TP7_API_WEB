from pydantic import BaseModel, ConfigDict

# Schéma pour la création d'une commune
class CommuneCreate(BaseModel):
    # dep: Le code du département auquel la commune appartient (type str)
    dep: str
    # cp: Le code postal de la commune (type str)
    cp: str
    # ville: Le nom de la ville ou de la commune (type str)
    ville: str

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    # 'from_attributes=True' signifie que les attributs de la base de données peuvent être directement utilisés.
    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'une commune
class Commune(CommuneCreate):
    # id: L'identifiant unique de la commune (type int, généralement généré par la base de données)
    id: int

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    # 'from_attributes=True' permet d'extraire facilement les attributs des objets de base de données.
    model_config = ConfigDict(from_attributes=True)
