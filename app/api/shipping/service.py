from datetime import datetime

shipments = []


def create_shipment(data):

    shipment = {
        "shipment_id": len(shipments) + 1,
        **data,
        "delivery_status": "Created",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    shipments.append(shipment)

    return shipment


def get_shipments():
    return shipments


def track_shipment(shipment_id):

    for shipment in shipments:

        if shipment["shipment_id"] == shipment_id:
            return shipment

    return {
        "error": "Shipment not found"
    }
