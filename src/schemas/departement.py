from pydantic import BaseModel, ConfigDict

# Schéma pour la création d'un département
class DepartementCreate(BaseModel):
    # code_dept: Le code du département, généralement une abréviation ou un identifiant unique (type str)
    code_dept: str
    # nom_dept: Le nom du département (type str)
    nom_dept: str
    # ordre_aff_dept: Ordre d'affichage ou de priorité du département (type int) - actuellement commenté
    # ordre_aff_dept: int  # Ce champ est commenté, mais peut être utilisé pour définir l'ordre d'affichage ou de priorité

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    # 'from_attributes=True' permet à Pydantic de mapper les attributs de la base de données à l'objet Pydantic.
    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'un département
class Departement(DepartementCreate):
    # Le modèle hérite des champs de DepartementCreate et n'ajoute pas de nouveaux champs supplémentaires.

    # Configuration du modèle : même logique que pour DepartementCreate
    model_config = ConfigDict(from_attributes=True)
