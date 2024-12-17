from pydantic import BaseModel, ConfigDict
from decimal import Decimal

# Schéma pour créer un conditionnement
class ConditionnementCreate(BaseModel):
    # libcondit: Le nom ou la description du conditionnement (type str)
    libcondit: str
    # poidscondit: Le poids du conditionnement (type int)
    poidscondit: int
    # prixcond: Le prix du conditionnement (type Decimal) - actuellement commenté
    # prixcond: Decimal  # À l'avenir, si nécessaire, on pourrait activer et utiliser ce champ
    # ordreimp: Ordre d'importance du conditionnement (type int)
    ordreimp: int

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    # 'from_attributes=True' permet de mapper facilement les données des attributs de la base de données.
    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'un conditionnement
class Conditionnement(ConditionnementCreate):
    # idcondit: L'identifiant unique du conditionnement dans la base de données (type int)
    idcondit: int

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    # 'from_attributes=True' permet d'extraire les attributs des objets de base de données facilement.
    model_config = ConfigDict(from_attributes=True)
