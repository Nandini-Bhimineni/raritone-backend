from fastapi import (
    APIRouter,
    HTTPException
)

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate
)

from app.api.products.service import (
    create_product,
    get_product,
    get_all_products,
    search_products,
    update_product,
    delete_product
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
def add_product(
    product: ProductCreate
):
    return create_product(
        product
    )


@router.get("/")
def list_products():
    return get_all_products()


@router.get("/search")
def search_product(
    keyword: str
):
    return search_products(
        keyword
    )


@router.get("/{product_id}")
def product_profile(
    product_id: int
):
    product = get_product(
        product_id
    )

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.put("/{product_id}")
def edit_product(
    product_id: int,
    product: ProductUpdate
):

    updated = update_product(
        product_id,
        product
    )

    if not updated:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated


@router.delete("/{product_id}")
def remove_product(
    product_id: int
):

    deleted = delete_product(
        product_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message":
        "Product deleted successfully"
    }