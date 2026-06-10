from app.models.product import Product


def create_product(db, product):
    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_product(db, product_id):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()


def search_products(db, keyword):
    return db.query(Product).filter(
        Product.name.ilike(f"%{keyword}%")
    ).all()


def update_product(db, product_obj, data):

    for key, value in data.dict(
        exclude_unset=True
    ).items():
        setattr(product_obj, key, value)

    db.commit()
    db.refresh(product_obj)

    return product_obj


def delete_product(db, product_obj):
    db.delete(product_obj)
    db.commit()