from fastapi import APIRouter
from app.schemas.inventory_schema import InventoryCreate
from app.api.inventory.service import *

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.get("/")
def get_inventory():
    return get_inventory_service()


@router.post("/")
def create_inventory(item: InventoryCreate):
    return create_inventory_service(item)


@router.get("/low-stock")
def low_stock():
    return low_stock_service()


@router.put("/{inventory_id}")
def update_inventory(
    inventory_id: int,
    item: InventoryCreate
):
    return update_inventory_service(
        inventory_id,
        item
    )


@router.delete("/{inventory_id}")
def delete_inventory(
    inventory_id: int
):
    return delete_inventory_service(
        inventory_id
    )