class Notification:
    def __init__(
        self,
        notification_id,
        user_id,
        title,
        message,
        notification_type
    ):
        self.notification_id = notification_id
        self.user_id = user_id
        self.title = title
        self.message = message
        self.notification_type = notification_type

