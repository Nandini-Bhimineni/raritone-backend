from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.category import Category
from app.schemas.category_schema import CategoryCreate, CategoryUpdate
from app.api.categories.service import (
    create_category as create_category_service,
    get_categories as get_categories_service,
    update_category as update_category_service,
    delete_category as delete_category_service
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**category.dict())
    return create_category_service(db, new_category)


@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return get_categories_service(db)


@router.put("/{category_id}")
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db)
):
    category_obj = db.query(Category).filter(Category.id == category_id).first()

    if not category_obj:
        raise HTTPException(status_code=404, detail="Category not found")

    return update_category_service(db, category_obj, category)


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    category_obj = db.query(Category).filter(Category.id == category_id).first()

    if not category_obj:
        raise HTTPException(status_code=404, detail="Category not found")

    delete_category_service(db, category_obj)

    return {"message": "Category deleted successfully"}