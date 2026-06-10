vendors = []
from datetime import datetime


def create_vendor(data):
    vendor = {
    "id": len(vendors) + 1,
    **data.dict(),
    "vendor_status": "Pending",
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    
}
    vendors.append(vendor)
    return vendor


def get_vendor(vendor_id):
    for vendor in vendors:
        if vendor["id"] == vendor_id:
            return vendor
    return None


def get_all_vendors():
    return vendors


def update_vendor(vendor_id, data):
    vendor = get_vendor(vendor_id)

    if not vendor:
        return None

    update_data = data.dict(exclude_unset=True)

    for key, value in update_data.items():
        vendor[key] = value
    vendor["updated_at"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S"
    )

    return vendor


def update_kyc(vendor_id, data):
    vendor = get_vendor(vendor_id)

    if not vendor:
        return None

    vendor["gst_number"] = data.gst_number
    vendor["kyc_document"] = data.kyc_document
    vendor["is_verified"] = True
    vendor["vendor_status"]="Active"
    vendor["updated_at"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S"
    )


    return vendor


def delete_vendor(vendor_id):
    global vendors

    vendor = get_vendor(vendor_id)

    if not vendor:
        return False

    vendors = [v for v in vendors if v["id"] != vendor_id]

    return True