class Notification:
    def __init__(
        self,
        notification_id,
        user_id,
        title,
        message,
        notification_type,
        priority,
        is_read,
        status,
        created_at,
        updated_at
    ):
        self.notification_id = notification_id
        self.user_id = user_id
        self.title = title
        self.message = message
        self.notification_type = notification_type
        self.priority = priority
        self.is_read = is_read
        self.status = status  # "read" or "unread"
        self.created_at = created_at
        self.updated_at = updated_at