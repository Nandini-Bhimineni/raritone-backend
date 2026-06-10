from datetime import datetime

products = []


def get_stock_alert(stock):
    if stock == 0:
        return "Out Of Stock"

    if stock <= 10:
        return "Low Stock"

    return "In Stock"


def create_product(data):

    product = {
        "id": len(products) + 1,

        **data.dict(),

        "stock_alert": get_stock_alert(
            data.stock
        ),

        "created_at": str(
            datetime.now()
        ),

        "updated_at": str(
            datetime.now()
        )
    }

    products.append(product)

    return product


def get_product(product_id):

    for product in products:

        if product["id"] == product_id:
            return product

    return None


def get_all_products():
    return products


def search_products(keyword):

    result = []

    for product in products:

        if keyword.lower() in product[
            "name"
        ].lower():

            result.append(product)

    return result


def update_product(
    product_id,
    data
):

    product = get_product(
        product_id
    )

    if not product:
        return None

    update_data = data.dict(
        exclude_unset=True
    )

    for key, value in update_data.items():

        product[key] = value

    product["stock_alert"] = (
        get_stock_alert(
            product["stock"]
        )
    )

    product["updated_at"] = str(
        datetime.now()
    )

    return product


def delete_product(product_id):

    global products

    product = get_product(
        product_id
    )

    if not product:
        return False

    products = [
        p for p in products
        if p["id"] != product_id
    ]

    return True