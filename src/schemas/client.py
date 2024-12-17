from pydantic import BaseModel, ConfigDict

class ClientCreate(BaseModel):

    emailcli: str | None = None
    model_config = ConfigDict(from_attributes=True)

class ClientResponse(BaseModel):
    nomcli: str | None = None
    emailcli: str | None = None
    
    model_config = ConfigDict(from_attributes=True)