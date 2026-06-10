from pydantic import BaseModel, Field
from typing import Literal

# Strict validation choices matching team specifications
PriorityType = Literal["Low", "Medium", "High", "Critical"]

NotificationType = Literal[
    "Order Update",
    "Payment Update",
    "Shipping Update",
    "Inventory Alert",
    "Vendor Alert",
    "Customer Alert",
    "System Alert"
]

class NotificationCreate(BaseModel):
    user_id: int
    title: str
    message: str
    notification_type: NotificationType
    priority: PriorityType = "Medium"

class NotificationResponse(BaseModel):
    notification_id: str
    user_id: int
    title: str
    message: str
    notification_type: NotificationType
    priority: PriorityType
    is_read: bool
    status: str
    created_at: str
    updated_at: str