from datetime import datetime
import uuid
from app.schemas import shipping_schema as schema

shipping_data = []

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_shipping_service(data: schema.ShippingCreate):
    t = get_timestamp()
    shipment = {
        "shipment_id": f"SHP-{uuid.uuid4().hex[:8].upper()}",
        "order_id": data.order_id,
        "customer_id": data.customer_id,
        "vendor_id": data.vendor_id,
        "courier": data.courier,
        "tracking_number": f"TRK-{uuid.uuid4().hex[:12].upper()}",
        "shipping_address": data.shipping_address,
        "status": "Pending",
        "estimated_delivery": data.estimated_delivery,
        "actual_delivery_date": None,
        "delivery_notes": data.delivery_notes,
        "created_at": t,
        "updated_at": t
    }
    shipping_data.append(shipment)
    return shipment

def get_all_shipping_service():
    return shipping_data

def get_shipping_by_id_service(shp_id: str):
    return next((s for s in shipping_data if s["shipment_id"] == shp_id), None)

def get_shipping_by_customer_service(c_id: int):
    return [s for s in shipping_data if s["customer_id"] == c_id]

def get_shipping_by_vendor_service(v_id: int):
    return [s for s in shipping_data if s["vendor_id"] == v_id]

def get_shipping_by_status_service(status: str):
    return [s for s in shipping_data if s["status"].lower() == status.lower()]

def get_shipping_by_tracking_service(trk_num: str):
    return next((s for s in shipping_data if s["tracking_number"] == trk_num), None)

def update_shipping_status_service(shp_id: str, status: str):
    s = get_shipping_by_id_service(shp_id)
    if not s:
        return None
    s["status"] = status
    s["updated_at"] = get_timestamp()
    if status == "Delivered":
        s["actual_delivery_date"] = datetime.now().strftime("%Y-%m-%d")
    return s

def get_shipping_analytics_service():
    status_counts = {
        "Pending": 0, "Packed": 0, "Dispatched": 0, 
        "In-Transit": 0, "Out For Delivery": 0, "Delivered": 0, "Cancelled": 0
    }
    courier_counts = {}
    
    for s in shipping_data:
        # Count by status
        if s["status"] in status_counts:
            status_counts[s["status"]] += 1
            
        # Count by courier company
        c_name = s["courier"]
        courier_counts[c_name] = courier_counts.get(c_name, 0) + 1
        
    return {
        "total_shipments": len(shipping_data),
        "by_status": status_counts,
        "by_courier": courier_counts
    }

def get_shipping_counts_service():
    return {
        "total": len(shipping_data),
        "pending": len([s for s in shipping_data if s["status"] in ["Pending", "Packed"]]),
        "delivered": len([s for s in shipping_data if s["status"] == "Delivered"])
    }