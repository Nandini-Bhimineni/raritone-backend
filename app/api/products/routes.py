from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate

from app.api.products.service import (
    create_product as create_product_service,
    get_product,
    search_products,
    update_product as update_product_service,
    delete_product as delete_product_service
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    new_product = Product(**product.dict())

    return create_product_service(
        db,
        new_product
    )


@router.get("/search")
def search_product(
    keyword: str,
    db: Session = Depends(get_db)
):
    return search_products(
        db,
        keyword
    )


@router.put("/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    product_obj = get_product(
        db,
        product_id
    )

    if not product_obj:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return update_product_service(
        db,
        product_obj,
        product
    )


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product_obj = get_product(
        db,
        product_id
    )

    if not product_obj:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    delete_product_service(
        db,
        product_obj
    )

    return {
        "message": "Product deleted successfully"
    }