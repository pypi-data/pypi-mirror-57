from abc import ABC, abstractmethod
import inspect
from typing import Optional

from django.conf import settings
from django.utils import translation
from render_block import render_block_to_string, BlockNotFound

from sitech_notifier.utils import get_notification_model
from .exceptions import DuplicateNotificationType


class BaseNotification(ABC):
    """
    Abstract base notification class.

    Subclass this to send a specific notification to the app users.
    Override template_name attribute to set a template for email/SMS
    notifications.
    """
    @property
    @abstractmethod
    def description(self):
        """Description of what causes the notification."""

    @property
    @abstractmethod
    def template_name(self):
        """Path to the notification template."""

    notification_type = None
    notification_types = {}

    def get_notification_link(self) -> Optional[str]:
        """
        Get URL linked to the notification.

        Override this method if you want your notification to be linked
        to some resource in your app, for example to the blog post
        if notification informs about a new comment.
        """
        return None

    @staticmethod
    @abstractmethod
    def get_context_from_event(event):
        """Get notification context from Event object."""

    def get_notification_language(self) -> str:
        """
        Language code in which notification will be sent.

        By default set to settings.LANGUAGE_CODE. Override this method
        to have dynamic notification language, for example based on targetted
        user's language, if your app provides such setting.
        """
        return settings.LANGUAGE_CODE

    def transform_html_body(self, html_body) -> str:
        """
        Transform HTML content of the notification.

        Override this method if you want to somehow change the HTML content
        of the notification, for example add CSS with library like Premailer.
        Method should return modified HTML body.
        """
        return html_body

    def get_extra_model_data(self):
        """
        Get extra model data.

        Override this method if you're using custom notification model
        and you want to pass extra data to it. Returned dict will be passed
        as additional kwargs in notification creation.
        """
        return {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if inspect.isabstract(cls):
            return

        if cls.notification_type is None:
            cls.notification_type = cls.__name__.lower()

        notification_type = cls.notification_type
        if notification_type in cls.notification_types:
            raise DuplicateNotificationType('Notification with such type is already defined.')
        cls.notification_types[notification_type] = cls.description

    def __init__(self, user, event):
        self.user = user
        self.event = event
        self.context = {'user': self.user}

    def send(self) -> None:
        from .tasks import notify_async
        notification = self._create()
        notify_async.delay(notification.id)

    def _create(self):
        self.context.update(**self.get_context_from_event(self.event))

        lang = self.get_notification_language()
        with translation.override(lang):
            link = self.get_notification_link()
            self.context.update({'link': link})
            short_body = render_block_to_string(
                self.template_name, 'short_body', self.context
            ).strip()
            subject = render_block_to_string(self.template_name, 'subject', self.context).strip()

            try:
                txt_message = render_block_to_string(
                    self.template_name, 'text_body', self.context
                ).strip()
            except BlockNotFound:
                txt_message = None
            try:
                html_message = render_block_to_string(
                    self.template_name, 'html_body', self.context
                ).strip()
            except BlockNotFound:
                html_message = None

        Notification = get_notification_model()
        return Notification.objects.create(
            notification_type=self.notification_type,
            event=self.event,
            user=self.user,
            subject=subject,
            short_body=short_body,
            full_body_text=txt_message,
            full_body_html=self.transform_html_body(html_message),
            link=link,
            **self.get_extra_model_data()
        )


def get_notification_types():
    """Get all defined notifications."""
    return BaseNotification.notification_types.keys()


def get_notification_description(notification_type):
    return BaseNotification.notification_types[notification_type].description
