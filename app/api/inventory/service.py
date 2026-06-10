from datetime import datetime

inventory_data = []


def get_inventory_service():
    return inventory_data


def create_inventory_service(item):

    inventory_item = item.dict()

    inventory_item["inventory_id"] = f"INV{len(inventory_data) + 1001}"

    inventory_item["created_at"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    inventory_item["updated_at"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    inventory_data.append(inventory_item)

    return {
        "message": "Inventory Added Successfully",
        "data": inventory_item
    }


def low_stock_service():

    return [
        product
        for product in inventory_data
        if product["quantity"] < 10
    ]


def update_inventory_service(
    inventory_id,
    item
):

    return {
        "message": f"Inventory {inventory_id} Updated Successfully",
        "updated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "data": item
    }


def delete_inventory_service(
    inventory_id
):

    return {
        "message": f"Inventory {inventory_id} Deleted Successfully"
    }