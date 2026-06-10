from fastapi import HTTPException

from app.models.category import Category


def create_category(db, category):

    try:
        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


def get_categories(db):
    return db.query(Category).all()


def update_category(db, category_obj, data):

    for key, value in data.dict(
        exclude_unset=True
    ).items():
        setattr(category_obj, key, value)

    try:
        db.commit()
        db.refresh(category_obj)

        return category_obj

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


def delete_category(db, category_obj):

    try:
        db.delete(category_obj)
        db.commit()

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )