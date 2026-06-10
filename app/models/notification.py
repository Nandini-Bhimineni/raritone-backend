class Notification:
    def __init__(
        self,
        notification_id,
        user_id,
        title,
        message,
        notification_type,
        priority,
        is_read
    ):
        self.notification_id = notification_id
        self.user_id = user_id
        self.title = title
        self.message = message
        self.notification_type = notification_type
        self.priority = priority
        self.is_read = is_read