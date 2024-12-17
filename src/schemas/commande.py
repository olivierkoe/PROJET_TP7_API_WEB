from pydantic import BaseModel, ConfigDict
from typing import Optional

# Schéma pour la création d'une commande
class CommandeCreate(BaseModel):
    # timbrecli: Représente un montant associé au client (peut être nul, de type float)
    timbrecli: Optional[float] = None
    # timbrecde: Représente un montant pour la commande (peut être nul, de type float)
    timbrecde: Optional[float] = None
    # nbcolis: Représente le nombre de colis (par défaut à 1, de type int)
    nbcolis: Optional[int] = 1
    # cheqcli: Représente le montant du chèque du client (peut être nul, de type float)
    cheqcli: Optional[float] = None
    # idcondit: Représente l'identifiant du conditionnement associé (par défaut à 0, de type int)
    idcondit: Optional[int] = 0
    # cdeComt: Représente un commentaire ou une description pour la commande (peut être nul, de type str)
    cdeComt: Optional[str] = None
    # barchive: Un indicateur d'archivage de la commande (par défaut à 0, de type int)
    barchive: Optional[int] = 0
    # bstock: Un indicateur de stock pour la commande (par défaut à 0, de type int)
    bstock: Optional[int] = 0

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    # 'from_attributes=True' indique que les attributs de la base de données peuvent être utilisés directement.
    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'une commande
class CommandeResponse(CommandeCreate):
    # codcde: Représente l'identifiant unique de la commande (de type int)
    codcde: int  # ID de la commande

    # Configuration du modèle : permet de dériver les attributs de la base de données.
    # 'from_attributes=True' indique que les attributs de la base de données peuvent être utilisés directement.
    model_config = ConfigDict(from_attributes=True)
