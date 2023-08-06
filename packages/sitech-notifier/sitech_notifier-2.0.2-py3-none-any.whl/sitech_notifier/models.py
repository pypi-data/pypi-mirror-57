from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    """Event model storing event type name, event target and an actor."""
    name = models.CharField(max_length=100)

    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='+')
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_ct', 'target_id')

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class AbstractNotification(models.Model):
    """
    Base notification model.

    Stores essential data for email, SMS and real-time notifications.
    Can be subclassed if any extra data is needed, if not, use provided
    Notification model.
    """
    notification_type = models.CharField(max_length=100)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name='notifications'
    )

    subject = models.TextField()

    short_body = models.TextField(
        verbose_name=_('Short body'),
        help_text=_('Short body with only necessary info, '
                    'used in real-time notifications')
    )

    full_body_text = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Full plaintext body')
    )

    full_body_html = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Full HTML body')
    )

    link = models.CharField(max_length=100, blank=True, null=True)

    is_new = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Notification(AbstractNotification):
    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        related_name='notifications',
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
