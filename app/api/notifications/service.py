from datetime import datetime

notifications = []


def create_notification(data):

    notification = {
        "notification_id": len(notifications) + 1,
        **data.dict(),
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    notifications.append(notification)

    return notification


def get_notifications():
    return notifications