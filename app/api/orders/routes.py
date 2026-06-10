from fastapi import APIRouter
from app.schemas.order_schema import OrderCreate
from app.api.orders.service import *

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/")
def get_orders():
    return get_orders_service()


@router.post("/")
def create_order(order: OrderCreate):
    return create_order_service(order)


@router.post("/return")
def return_order():
    return return_order_service()


@router.get("/{order_id}")
def get_order(order_id: int):
    return {
        "order_id": order_id
    }


@router.put("/{order_id}")
def update_order(order_id: int):
    return update_order_service(order_id)


@router.delete("/{order_id}")
def delete_order(order_id: int):
    return delete_order_service(order_id)