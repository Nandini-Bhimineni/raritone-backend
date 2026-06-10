from fastapi import APIRouter, HTTPException
from app.schemas.shipping_schema import ShippingCreate, ShippingResponse
from app.api.shipping import service

router = APIRouter(prefix="/shipping", tags=["Shipping"])

@router.post("/", response_model=ShippingResponse)
def create_shipping(data: ShippingCreate):
    return service.create_shipping_service(data)

@router.get("/", response_model=list[ShippingResponse])
def get_all_shipping():
    return service.get_all_shipping_service()

@router.get("/count")
def get_shipping_count():
    counts = service.get_shipping_counts_service()
    return {"count": counts["total"]}

@router.get("/pending-count")
def get_pending_count():
    counts = service.get_shipping_counts_service()
    return {"pending_count": counts["pending"]}

@router.get("/delivered-count")
def get_delivered_count():
    counts = service.get_shipping_counts_service()
    return {"delivered_count": counts["delivered"]}

@router.get("/status/{status}", response_model=list[ShippingResponse])
def get_shipping_by_status(status: str):
    return service.get_shipping_by_status_service(status)

@router.get("/tracking/{tracking_number}", response_model=ShippingResponse)
def get_shipping_by_tracking(tracking_number: str):
    s = service.get_shipping_by_tracking_service(tracking_number)
    if not s: raise HTTPException(status_code=404, detail="Tracking number not found")
    return s

@router.get("/customer/{customer_id}", response_model=list[ShippingResponse])
def get_customer_shipping(customer_id: int):
    return service.get_shipping_by_customer_service(customer_id)

@router.get("/vendor/{vendor_id}", response_model=list[ShippingResponse])
def get_vendor_shipping(vendor_id: int):
    return service.get_shipping_by_vendor_service(vendor_id)

@router.get("/{shipment_id}", response_model=ShippingResponse)
def get_shipping_by_id(shipment_id: str):
    s = service.get_shipping_by_id_service(shipment_id)
    if not s: raise HTTPException(status_code=404, detail="Shipment not found")
    return s

# --- STATUS UPDATES ---
@router.put("/{shipment_id}/packed", response_model=ShippingResponse)
def status_packed(shipment_id: str):
    s = service.update_shipping_status_service(shipment_id, "Packed")
    if not s: raise HTTPException(status_code=404, detail="Shipment not found")
    return s

@router.put("/{shipment_id}/dispatch", response_model=ShippingResponse)
def status_dispatch(shipment_id: str):
    s = service.update_shipping_status_service(shipment_id, "Dispatched")
    if not s: raise HTTPException(status_code=404, detail="Shipment not found")
    return s

@router.put("/{shipment_id}/in-transit", response_model=ShippingResponse)
def status_in_transit(shipment_id: str):
    s = service.update_shipping_status_service(shipment_id, "In-Transit")
    if not s: raise HTTPException(status_code=404, detail="Shipment not found")
    return s

@router.put("/{shipment_id}/out-for-delivery", response_model=ShippingResponse)
def status_out_for_delivery(shipment_id: str):
    s = service.update_shipping_status_service(shipment_id, "Out For Delivery")
    if not s: raise HTTPException(status_code=404, detail="Shipment not found")
    return s

@router.put("/{shipment_id}/delivered", response_model=ShippingResponse)
def status_delivered(shipment_id: str):
    s = service.update_shipping_status_service(shipment_id, "Delivered")
    if not s: raise HTTPException(status_code=404, detail="Shipment not found")
    return s

@router.put("/{shipment_id}/cancel", response_model=ShippingResponse)
def status_cancel(shipment_id: str):
    s = service.update_shipping_status_service(shipment_id, "Cancelled")
    if not s: raise HTTPException(status_code=404, detail="Shipment not found")
    return s

@router.get("/analytics")
def get_shipping_analytics():
    return service.get_shipping_analytics_service()