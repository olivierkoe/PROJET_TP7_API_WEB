from fastapi import APIRouter

#Create = POST
#Read = GET
#Update = PUT
#Delete = DELETE

router_client = APIRouter()


@router_client.get("/clients")
async def get_clients():
    return [{"message": "Liste des clients"}]

@router_client.post("/clients")
async def get_clients():
    return [{"message": "Liste des clients"}]