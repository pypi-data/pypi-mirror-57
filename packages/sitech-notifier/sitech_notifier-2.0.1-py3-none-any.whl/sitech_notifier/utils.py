from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from . import settings as notifier_settings


def get_pusher_client():
    from pusher import Pusher
    return Pusher(
        app_id=settings.PUSHER_APP_ID,
        key=settings.PUSHER_KEY,
        secret=settings.PUSHER_SECRET,
        cluster=getattr(settings, 'PUSHER_CLUSTER', None),
        **getattr(settings, 'PUSHER_OPTIONS', {})
    )


def get_notification_model():
    try:
        return django_apps.get_model(notifier_settings.NOTIFICATION_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "SITECH_NOTIFIER_NOTIFICATION_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "SITECH_NOTIFIER_NOTIFICATION_MODEL refers to model '%s' "
            "that has not been installed".format(notifier_settings.NOTIFICATION_MODEL)
        )
