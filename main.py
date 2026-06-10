from fastapi import FastAPI

from app.api.vendors.routes import router as vendor_router
from app.api.customers.routes import router as customer_router

app = FastAPI(title="Raritone Backend")

app.include_router(vendor_router)
app.include_router(customer_router)