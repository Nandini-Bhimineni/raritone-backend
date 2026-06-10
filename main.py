from fastapi import FastAPI

from app.api.inventory.routes import router as inventory_router
from app.api.orders.routes import router as order_router
from app.api.vendors.routes import router as vendor_router
from app.api.customers.routes import router as customer_router

app = FastAPI(
    title="Raritone Backend"
)

# Inventory Module
app.include_router(inventory_router)

# Orders Module
app.include_router(order_router)

# Vendor Module
app.include_router(vendor_router)

# Customer Module
app.include_router(customer_router)


@app.get("/")
def home():
    return {
        "message": "Raritone Backend Running"
    }


@app.get("/test")
def test():
    return {
        "message": "Test Working"
    }
