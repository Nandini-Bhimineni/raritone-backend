from fastapi import APIRouter

from app.schemas.notification_schema import (
    NotificationCreate
)

from app.api.notifications.service import (
    create_notification,
    get_notifications
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post("/")
def send_notification(
    data: NotificationCreate
):
    return create_notification(data)


@router.get("/")
def list_notifications():
    return get_notifications()
