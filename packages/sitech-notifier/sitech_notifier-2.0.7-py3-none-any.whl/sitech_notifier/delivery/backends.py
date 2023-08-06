from abc import ABC, abstractmethod

from django.conf import settings
from django.core.mail import send_mail

from sitech_notifier.utils import get_pusher_client, get_notification_model


class NotificationDeliveryBackend(ABC):
    """Base class for notification delivery backends."""
    @abstractmethod
    def perform_send(self, notification):
        """
        Send the notification through a specific medium.

        Override this method to specify how the notification will be sent.
        """

    def send_notification(self, notification_id) -> None:
        """
        Send notification to the user.

        Fetch the notification and deliver it through the specific medium,
        i.e. email or SMS.
        """
        Notification = get_notification_model()
        notification = Notification.objects.select_related('user').get(id=notification_id)
        if not self.notification_enabled(notification):
            return
        self.perform_send(notification)

    def notification_enabled(self, notification) -> bool:
        """
        Check if user has enabled notifications.

        Override this method if your app stores information
        about enabling specific types of notifications for the user.
        """
        return True


class EmailDeliveryBackend(NotificationDeliveryBackend):
    def perform_send(self, notification) -> None:
        send_mail(
            notification.subject,
            notification.full_body_text,
            settings.DEFAULT_FROM_EMAIL,
            [notification.user.email],
            html_message=notification.full_body_html
        )


class BaseSMSDeliveryBackend(NotificationDeliveryBackend):
    """Base class for SMS delivery."""
    def perform_send(self, notification) -> None:
        """
        Send SMS notification.

        This backend will not work out of the box. User of the library
        has to subclass it and integrate with SMS gateway and provide user's
        mobile number.
        """


class PusherDeliveryBackend(NotificationDeliveryBackend):
    """
    Realtime notification delivery via Pusher.

    To enable this backend, following settings have to be set:
    - PUSHER_APP_ID
    - PUSHER_KEY
    - PUSHER_SECRET
    - PUSHER_CLUSTER (optional, set if other than default us-east-1)
    - PUSHER_OPTIONS (optional, additional kwargs for Pusher instance)
    """
    def __init__(self):
        self.client = get_pusher_client()

    def perform_send(self, notification):
        self.client.trigger(
            'private-user-{}'.format(notification.user.id),
            'new-notification',
            {
                'message': notification.short_body,
                'link': notification.link
            }
        )
