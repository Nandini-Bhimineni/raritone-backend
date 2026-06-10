from fastapi import (
    APIRouter,
    HTTPException
)

from app.schemas.notification_schema import (
    NotificationCreate
)

from app.api.notifications.service import *

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post("/")
def create_notification(
    notification: NotificationCreate
):
    return create_notification_service(
        notification
    )


@router.get("/")
def get_notifications():
    return get_notifications_service()


@router.get("/count")
def notification_count():
    return get_notification_count_service()


@router.get("/unread")
def unread_notifications():
    return (
        get_unread_notifications_service()
    )


@router.put("/read-all")
def mark_all_read():
    return mark_all_read_service()


@router.delete("/all")
def delete_all():
    return (
        delete_all_notifications_service()
    )


@router.get("/search")
def search_notifications(
    keyword: str
):
    return search_notifications_service(
        keyword
    )


@router.get("/user/{user_id}")
def user_notifications(
    user_id: int
):
    return (
        get_user_notifications_service(
            user_id
        )
    )


@router.get("/{notification_id}")
def get_notification(
    notification_id: str
):

    notification = (
        get_notification_service(
            notification_id
        )
    )

    if not notification:

        raise HTTPException(
            status_code=404,
            detail=
            "Notification not found"
        )

    return notification


@router.put("/{notification_id}/read")
def mark_read(
    notification_id: str
):

    notification = (
        mark_read_service(
            notification_id
        )
    )

    if not notification:

        raise HTTPException(
            status_code=404,
            detail=
            "Notification not found"
        )

    return notification


@router.delete("/{notification_id}")
def delete_notification(
    notification_id: str
):

    deleted = (
        delete_notification_service(
            notification_id
        )
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail=
            "Notification not found"
        )

    return {
        "message":
        "Notification deleted successfully"
    }