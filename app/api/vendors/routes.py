from fastapi import APIRouter, HTTPException

from app.schemas.vendor_schema import (
    VendorCreate,
    VendorUpdate,
    KYCUpdate
)

from app.api.vendors.service import (
    create_vendor,
    get_vendor,
    get_all_vendors,
    update_vendor,
    update_kyc,
    delete_vendor
)

router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"]
)


@router.post("/")
def add_vendor(vendor: VendorCreate):
    return create_vendor(vendor)


@router.get("/")
def list_vendors():
    return get_all_vendors()


@router.get("/{vendor_id}")
def vendor_profile(vendor_id: int):
    vendor = get_vendor(vendor_id)

    if not vendor:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return vendor


@router.put("/{vendor_id}")
def edit_vendor(vendor_id: int, vendor: VendorUpdate):
    updated = update_vendor(vendor_id, vendor)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return updated


@router.put("/{vendor_id}/kyc")
def vendor_kyc(vendor_id: int, kyc: KYCUpdate):
    updated = update_kyc(vendor_id, kyc)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return updated


@router.delete("/{vendor_id}")
def remove_vendor(vendor_id: int):
    deleted = delete_vendor(vendor_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return {
        "message": "Vendor deleted successfully"
    }