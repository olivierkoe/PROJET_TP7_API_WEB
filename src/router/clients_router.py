from fastapi import APIRouter


router_client = APIRouter()

@router_client.get("/clients")
async def get_clients():
    return [{"message": "Liste des clients"}]