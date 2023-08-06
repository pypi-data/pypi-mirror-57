from typing import Callable, Type, Iterable, Union, Optional, Dict

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from sitech_notifier.notifications import BaseNotification

from .models import Event as EventModel


HandlerReturnType = Union[AbstractBaseUser, Iterable[AbstractBaseUser]]


class BaseEvent:
    name: Optional[str] = None
    registered_events: Dict[str, Type['BaseEvent']] = {}

    @staticmethod
    def side_effects(event: 'EventModel') -> None:
        """Side effects called during handling the event."""
        pass

    def __init_subclass__(cls, **kwargs) -> None:
        if cls.name is None:
            cls.name = cls.__name__.lower()
        if cls.name in cls.registered_events:
            raise ValueError('Event with that name is already registered.')
        cls.registered_events[cls.name] = cls

    def __init__(
            self,
            target: 'models.Model',
            actor: Optional['AbstractBaseUser'] = None
    ) -> None:
        self.target = target
        self.actor = actor

    def emit(self) -> None:
        """
        Emit the event.

        When event is emitted, notifications connected by
        @register_notification decorator are sent and side effects
        are called in celery tasks.
        """
        from .tasks import handle_event, handle_side_effects
        event = EventModel.objects.create(name=self.name, target=self.target, actor=self.actor)
        handle_event.delay(self.name, event.id)
        handle_side_effects.delay(self.name, event.id)


def register_notification(notification_class: Type[BaseNotification]) -> Callable:
    """
    Register notification as callback to the event.

    Decorated methods have to return User or iterable of Users
    to whom the notification will be sent and kwargs passed to the
    notification. Use HandlerReturnType alias as a decorated function
    return type to avoid mistakes.
    """
    if notification_class.get_context_from_event is BaseNotification.get_context_from_event:
        raise TypeError(
            'Notification being registered must have get_context_from_event method overridden.'
        )

    def inner(func: Callable[..., HandlerReturnType]):
        if hasattr(func, 'for_notification'):
            func.for_notification.append(notification_class)
        else:
            func.for_notification = [notification_class]
        return func
    return inner
