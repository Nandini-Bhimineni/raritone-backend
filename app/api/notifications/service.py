from datetime import datetime

notifications_data = []


def get_notifications_service():
    return notifications_data


def get_notification_service(notification_id):

    for notification in notifications_data:

        if notification["notification_id"] == notification_id:
            return notification

    return None


def create_notification_service(data):

    notification = {
        "notification_id":
        f"NOT{len(notifications_data)+1001}",

        "user_id": data.user_id,
        "title": data.title,
        "message": data.message,
        "notification_type":
        data.notification_type,

        "priority": data.priority,

        "is_read": False,

        "created_at":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "updated_at":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    notifications_data.append(notification)

    return notification


def mark_read_service(notification_id):

    notification = get_notification_service(
        notification_id
    )

    if not notification:
        return None

    notification["is_read"] = True

    notification["updated_at"] = (
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    return notification


def delete_notification_service(
    notification_id
):
    global notifications_data

    notification = (
        get_notification_service(
            notification_id
        )
    )

    if not notification:
        return False

    notifications_data = [
        n for n in notifications_data
        if n["notification_id"]
        != notification_id
    ]

    return True


def get_notification_count_service():

    total = len(notifications_data)

    unread = len(
        [
            n
            for n in notifications_data
            if not n["is_read"]
        ]
    )

    return {
        "total_notifications": total,
        "unread_notifications": unread
    }


def get_user_notifications_service(
    user_id
):

    return [
        n
        for n in notifications_data
        if n["user_id"] == user_id
    ]


def get_unread_notifications_service():

    return [
        n
        for n in notifications_data
        if not n["is_read"]
    ]


def mark_all_read_service():

    for notification in notifications_data:

        notification["is_read"] = True

        notification["updated_at"] = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

    return {
        "message":
        "All notifications marked as read"
    }


def delete_all_notifications_service():

    notifications_data.clear()

    return {
        "message":
        "All notifications deleted"
    }


def search_notifications_service(
    keyword
):

    keyword = keyword.lower()

    return [
        n
        for n in notifications_data
        if keyword in n["title"].lower()
        or keyword in n["message"].lower()
    ]