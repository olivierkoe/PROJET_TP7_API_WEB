from pydantic import BaseModel, ConfigDict
from typing import Optional

# Schéma pour la création d'un objet
class ObjetCreate(BaseModel):
    # codobj: L'identifiant de l'objet (généralement généré automatiquement par la base de données, donc optionnel)
    codobj: Optional[int] = None
    # libobj: Le libellé de l'objet (peut être nul, de type str)
    libobj: Optional[str] = None
    # tailleobj: La taille de l'objet (peut être nul, de type str)
    tailleobj: Optional[str] = None
    # puobj: Le prix unitaire de l'objet (par défaut à 0.0000, de type float)
    puobj: Optional[float] = 0.0000
    # poidsobj: Le poids de l'objet (par défaut à 0.0000, de type float)
    poidsobj: Optional[float] = 0.0000
    # indispobj: Indicateur d'indisponibilité de l'objet (par défaut à 0, de type int)
    indispobj: Optional[int] = 0
    # o_imp: Un indicateur pour l'exportation de l'objet (par défaut à 0, de type int)
    o_imp: Optional[int] = 0
    # o_aff: Un indicateur pour l'affichage de l'objet (par défaut à 0, de type int)
    o_aff: Optional[int] = 0
    # o_cartp: Un indicateur pour l'affichage du panier (par défaut à 0, de type int)
    o_cartp: Optional[int] = 0
    # points: Un nombre de points associés à l'objet (par défaut à 0, de type int)
    points: Optional[int] = 0
    # o_ordre_aff: L'ordre d'affichage de l'objet (par défaut à 0, de type int)
    o_ordre_aff: Optional[int] = 0
    # condit: La relation avec l'objet de conditionnement (peut être nul, de type list de ObjetCond)
    condit: Optional[list] = []

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'un objet (inclut l'ID de l'objet après création)
class ObjetResponse(ObjetCreate):
    # codobj: L'identifiant unique de l'objet (de type int)
    codobj: int  # ID de l'objet

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    model_config = ConfigDict(from_attributes=True)
