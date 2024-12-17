from pydantic import BaseModel, ConfigDict

# Modèle pour créer un client
class ClientCreate(BaseModel):
<<<<<<< HEAD
    # Le nom du client (nomcli) est une chaîne de caractères qui peut être vide (None)
    nomcli: str | None = None
    # L'email du client (emailcli) est une chaîne de caractères qui peut être vide (None)
    emailcli: str | None = None

    # Configuration du modèle : permet de définir le comportement pour les attributs.
    # 'from_attributes=True' indique que les attributs de ce modèle peuvent être dérivés de la base de données
=======

    emailcli: str | None = None
>>>>>>> 9a21b7416216b13ecd5f7c7c41edacb9d0b1b4bf
    model_config = ConfigDict(from_attributes=True)

# Modèle pour répondre avec les informations d'un client
class ClientResponse(BaseModel):
    # Le nom du client (nomcli) est une chaîne de caractères qui peut être vide (None)
    nomcli: str | None = None
    # L'email du client (emailcli) est une chaîne de caractères qui peut être vide (None)
    emailcli: str | None = None

    # Configuration du modèle : permet de définir le comportement pour les attributs.
    # 'from_attributes=True' indique que les attributs de ce modèle peuvent être dérivés de la base de données
    model_config = ConfigDict(from_attributes=True)
