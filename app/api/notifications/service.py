from datetime import datetime
from app.schemas import notification_schema as schema

notifications_data = []


def get_notifications_service():
    return notifications_data


def get_notification_service(notification_id):
    for notification in notifications_data:
        if notification["notification_id"] == notification_id:
            return notification
    return None


def create_notification_service(data):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    notification = {
        "notification_id": f"NOT{len(notifications_data)+1001}",
        "user_id": data.user_id,
        "title": data.title,
        "message": data.message,
        "notification_type": data.notification_type,
        "priority": data.priority,
        "is_read": False,
        "status": "unread",  # 🟢 Added Required Status Field
        "created_at": current_time,
        "updated_at": current_time
    }

    notifications_data.append(notification)
    return notification


def mark_read_service(notification_id):
    notification = get_notification_service(notification_id)
    if not notification:
        return None

    notification["is_read"] = True
    notification["status"] = "read"  # 🟢 Synced Status Field
    notification["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return notification


def delete_notification_service(notification_id):
    global notifications_data
    notification = get_notification_service(notification_id)
    if not notification:
        return False

    notifications_data = [
        n for n in notifications_data
        if n["notification_id"] != notification_id
    ]
    return True


def get_notification_count_service():
    total = len(notifications_data)
    unread = len([n for n in notifications_data if not n["is_read"]])
    read = len([n for n in notifications_data if n["is_read"]])

    return {
        "total_notifications": total,
        "unread_notifications": unread,
        "read_notifications": read  # 🟢 Enhanced to match global count spec
    }


def get_user_notifications_service(user_id):
    return [n for n in notifications_data if n["user_id"] == user_id]


def get_unread_notifications_service():
    return [n for n in notifications_data if not n["is_read"]]


def mark_all_read_service():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for notification in notifications_data:
        notification["is_read"] = True
        notification["status"] = "read"  # 🟢 Synced Status Field
        notification["updated_at"] = current_time

    return {"message": "All notifications marked as read"}


def delete_all_notifications_service():
    notifications_data.clear()
    return {"message": "All notifications deleted"}


def search_notifications_service(keyword):
    keyword = keyword.lower()
    return [
        n for n in notifications_data
        if keyword in n["title"].lower() or keyword in n["message"].lower()
    ]


# ==========================================
# 🟢 MINIMAL ADDITIONS FOR MISSING SPEC RULES
# ==========================================

def get_notifications_by_filters_service(notification_type=None, priority=None):
    """Filter implementation matching module specifications"""
    results = notifications_data
    if notification_type:
        results = [n for n in results if n["notification_type"].lower() == notification_type.lower()]
    if priority:
        results = [n for n in results if n["priority"].lower() == priority.lower()]
    return results


def get_notification_analytics_service():
    """Analytics implementation providing breakdowns by metric classes"""
    priority_counts = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}
    type_counts = {
        "Order Update": 0, "Payment Update": 0, "Shipping Update": 0,
        "Inventory Alert": 0, "Vendor Alert": 0, "Customer Alert": 0, "System Alert": 0
    }
    
    for n in notifications_data:
        if n["priority"] in priority_counts:
            priority_counts[n["priority"]] += 1
        if n["notification_type"] in type_counts:
            type_counts[n["notification_type"]] += 1
            
    return {
        "total_count": len(notifications_data),
        "by_priority": priority_counts,
        "by_type": type_counts
    }