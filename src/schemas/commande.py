from pydantic import BaseModel, ConfigDict
from typing import Optional

# Schéma pour la création d'une commande
class CommandeCreate(BaseModel):
    # codcli: int
    # datcde: str
    timbrecli: Optional[float] = None
    timbrecde: Optional[float] = None
    nbcolis: Optional[int] = 1
    cheqcli: Optional[float] = None
    idcondit: Optional[int] = 0
    cdeComt: Optional[str] = None
    barchive: Optional[int] = 0
    bstock: Optional[int] = 0

    model_config = ConfigDict(from_attributes=True)

# Schéma pour la réponse d'une commande
class CommandeResponse(CommandeCreate):
    codcde: int  # ID de la commande

    model_config = ConfigDict(from_attributes=True)