from typing import Iterable

from celery import shared_task
from django.utils.module_loading import import_string

from .events import BaseEvent
from .models import Event as EventModel
from . import settings


@shared_task
def notify_async(notification_id):
    backends = settings.SITECH_NOTIFIER_DELIVERY_BACKENDS
    for backend_path in backends:
        deliver_async.delay(backend_path, notification_id)


@shared_task
def deliver_async(backend_path, notification_id):
    backend = import_string(backend_path)()
    backend.send_notification(notification_id)


@shared_task
def handle_event(event_name, event_id):
    """Send notifications connected to the event."""
    event_class = BaseEvent.registered_events[event_name]
    event = EventModel.objects.get(pk=event_id)

    notification_handlers = [
        getattr(event_class, func) for func in dir(event_class)
        if hasattr(getattr(event_class, func), 'for_notification')
    ]
    for handler in notification_handlers:
        for notification_class in handler.for_notification:
            recipients = handler(event)
            if not isinstance(recipients, Iterable):
                recipients = [recipients]
            for user in recipients:
                notification_class(user, event).send()


@shared_task
def handle_side_effects(event_name, event_id):
    """Call side effects connected to the event."""
    event_class = BaseEvent.registered_events[event_name]
    event = EventModel.objects.get(pk=event_id)

    event_class.side_effects(event)
