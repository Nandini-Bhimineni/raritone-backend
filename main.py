from fastapi import FastAPI

from app.api.inventory.routes import router as inventory_router
from app.api.orders.routes import router as order_router

app = FastAPI(
    title="Raritone Backend"
)

app.include_router(inventory_router)
app.include_router(order_router)

@app.get("/")
def home():
    return {"message": "Raritone Backend Running"}

@app.get("/test")
def test():
    return {"message": "Test Working"}