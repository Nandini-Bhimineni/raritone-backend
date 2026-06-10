from fastapi import APIRouter

from app.api.shipping.service import (
    create_shipment,
    get_shipments,
    track_shipment
)

router = APIRouter(
    prefix="/shipping",
    tags=["Shipping"]
)


@router.post("/")
def shipment():

    data = {
        "courier": "Delhivery"
    }

    return create_shipment(data)


@router.get("/")
def shipments():
    return get_shipments()


@router.get("/{shipment_id}")
def tracking(
    shipment_id: int
):
    return track_shipment(
        shipment_id
    )
