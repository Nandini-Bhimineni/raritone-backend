from datetime import datetime
from app.api.inventory.service import inventory_data

orders_data = []


def get_orders_service():
    return orders_data


def create_order_service(order):

    for product in inventory_data:

        if product["product_id"] == order.product_id:

            if product["quantity"] < order.quantity:

                return {
                    "error": "Out Of Stock"
                }

            product["quantity"] -= order.quantity

            order_data = order.dict()

            order_data["order_id"] = (
                f"ORD{len(orders_data) + 1001}"
            )

            order_data["created_at"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            orders_data.append(order_data)

            return {
                "message": "Order Created Successfully",
                "remaining_stock": product["quantity"],
                "order": order_data
            }

    return {
        "error": "Product Not Found"
    }


def return_order_service():

    return {
        "message": "Order Returned Successfully"
    }


def update_order_service(order_id):

    return {
        "message": f"Order {order_id} Updated Successfully"
    }


def delete_order_service(order_id):

    return {
        "message": f"Order {order_id} Cancelled Successfully"
    }