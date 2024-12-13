
from fastapi import FastAPI
from router.clients_router import router_client

app = FastAPI()
app.include_router(router_client)


@app.get("/")
def read_root():
    return {"Hello": "World"}

