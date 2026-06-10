from pydantic import BaseModel


class NotificationCreate(BaseModel):
    user_id: int
    title: str
    message: str
    notification_type: str
    priority: str = "Medium"


class NotificationResponse(BaseModel):
    notification_id: str
    user_id: int
    title: str
    message: str
    notification_type: str
    priority: str
    is_read: bool
    created_at: str
    updated_at: str


class NotificationSearch(BaseModel):
    keyword: str