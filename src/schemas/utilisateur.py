from datetime import datetime, date
from pydantic import BaseModel, ConfigDict, Field

# Modèle pour créer un utilisateur
class UtilisateurCreate(BaseModel):
    """
    Modèle pour créer un utilisateur.
    """
    nom_utilisateur: str | None = Field(None, description="Nom de l'utilisateur")
    prenom_utilisateur: str | None = Field(None, description="Prénom de l'utilisateur")
    username: str | None = Field(None, description="Identifiant ou pseudonyme")

    model_config = ConfigDict(from_attributes=True)


# Modèle pour répondre avec les informations d'un utilisateur
class UtilisateurResponse(BaseModel):
    """
    Modèle pour la réponse utilisateur.
    """
    nom_utilisateur: str | None = Field(None, description="Nom de l'utilisateur")
    prenom_utilisateur: str | None = Field(None, description="Prénom de l'utilisateur")
    username: str | None = Field(None, description="Identifiant ou pseudonyme")
    date_insc_utilisateur: date = Field(
        default_factory=lambda: datetime.now().date(),
        description="Date d'inscription de l'utilisateur, définie automatiquement à la création",
    )

    model_config = ConfigDict(from_attributes=True)
