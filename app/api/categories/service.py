from app.models.category import Category


def create_category(db, category):
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db):
    return db.query(Category).all()


def update_category(db, category_obj, data):
    for key, value in data.dict(exclude_unset=True).items():
        setattr(category_obj, key, value)

    db.commit()
    db.refresh(category_obj)

    return category_obj


def delete_category(db, category_obj):
    db.delete(category_obj)
    db.commit()