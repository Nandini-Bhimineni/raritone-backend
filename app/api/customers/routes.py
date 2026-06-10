from fastapi import APIRouter, HTTPException

from app.schemas.customer_schema import (
    CustomerCreate,
    CustomerUpdate
)

from app.api.customers.service import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/")
def add_customer(customer: CustomerCreate):
    return create_customer(customer)


@router.get("/")
def list_customers():
    return get_all_customers()


@router.get("/{customer_id}")
def customer_profile(customer_id: int):
    customer = get_customer(customer_id)

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.put("/{customer_id}")
def edit_customer(
    customer_id: int,
    customer: CustomerUpdate
):
    updated = update_customer(
        customer_id,
        customer
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return updated

@router.get("/{customer_id}/orders")
def customer_orders(customer_id: int):
    return {
        "customer_id": customer_id,
        "orders": []
    }


@router.get("/{customer_id}/reviews")
def customer_reviews(customer_id: int):
    return {
        "customer_id": customer_id,
        "reviews": []
    } 


@router.delete("/{customer_id}")
def remove_customer(customer_id: int):
    deleted = delete_customer(customer_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "message": "Customer deleted successfully"
    }