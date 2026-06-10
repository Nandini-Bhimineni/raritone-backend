from fastapi import (
    APIRouter,
    HTTPException
)

from app.schemas.category_schema import (
    CategoryCreate,
    CategoryUpdate
)

from app.api.categories.service import (
    create_category,
    get_category,
    get_all_categories,
    update_category,
    delete_category
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post("/")
def add_category(
    category: CategoryCreate
):
    return create_category(
        category
    )


@router.get("/")
def list_categories():
    return get_all_categories()


@router.get("/{category_id}")
def category_profile(
    category_id: int
):

    category = get_category(
        category_id
    )

    if not category:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@router.put("/{category_id}")
def edit_category(
    category_id: int,
    category: CategoryUpdate
):

    updated = update_category(
        category_id,
        category
    )

    if not updated:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return updated


@router.delete("/{category_id}")
def remove_category(
    category_id: int
):

    deleted = delete_category(
        category_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "message":
        "Category deleted successfully"
    }