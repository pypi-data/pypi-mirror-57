from django.conf import settings


SITECH_NOTIFIER_DELIVERY_BACKENDS = getattr(settings, 'SITECH_NOTIFIER_DELIVERY_BACKENDS', [
    'sitech_notifier.delivery.backends.EmailDeliveryBackend'
])

NOTIFICATION_MODEL = getattr(
    settings, 'SITECH_NOTIFIER_NOTIFICATION_MODEL', 'sitech_notifier.Notification'
)
