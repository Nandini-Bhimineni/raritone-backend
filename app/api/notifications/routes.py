from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.schemas.notification_schema import NotificationCreate, NotificationResponse
from app.api.notifications import service

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.post("/", response_model=NotificationResponse)
def create_notification(notification: NotificationCreate):
    return service.create_notification_service(notification)

@router.get("/", response_model=list[NotificationResponse])
def get_notifications():
    return service.get_notifications_service()

@router.get("/count")
def notification_count():
    return service.get_notification_count_service()

# 🟢 NEW: Added to satisfy the global Analytics API requirement
@router.get("/analytics")
def notification_analytics():
    return service.get_notification_analytics_service()

@router.get("/search", response_model=list[NotificationResponse])
def search_notifications(keyword: str):
    return service.search_notifications_service(keyword)

# 🟢 NEW: Added to satisfy the global Filter APIs requirement
@router.get("/filter", response_model=list[NotificationResponse])
def filter_notifications(
    type: Optional[str] = None,
    priority: Optional[str] = None
):
    return service.get_notifications_by_filters_service(notification_type=type, priority=priority)

@router.get("/unread", response_model=list[NotificationResponse])
def unread_notifications():
    return service.get_unread_notifications_service()

@router.get("/user/{user_id}", response_model=list[NotificationResponse])
def user_notifications(user_id: int):
    return service.get_user_notifications_service(user_id)

@router.get("/{notification_id}", response_model=NotificationResponse)
def get_notification(notification_id: str):
    notification = service.get_notification_service(notification_id)
    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )
    return notification

@router.put("/read-all")
def mark_all_read():
    return service.mark_all_read_service()

@router.put("/{notification_id}/read", response_model=NotificationResponse)
def mark_read(notification_id: str):
    notification = service.mark_read_service(notification_id)
    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )
    return notification

@router.delete("/all")
def delete_all():
    return service.delete_all_notifications_service()

@router.delete("/{notification_id}")
def delete_notification(notification_id: str):
    deleted = service.delete_notification_service(notification_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )
    return {
        "message": "Notification deleted successfully"
    }