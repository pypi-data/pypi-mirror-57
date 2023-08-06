from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag('sitech_notifier/pusher-notifications.html', takes_context=True)
def enable_pusher_notifications(context):
    """
    Enable pusher notifications.

    Use this tag to enable pusher notifications. Note that PUSHER_KEY setting
    must be set.

    It' also required to provide NOTIFICATION_CALLBACK
    javascript function in the same template.

    For example:
    const NOTIFICATION_CALLBACK = function(data) {
        console.log(data.message);
    }
    """
    request = context['request']
    user = request.user

    if not user.is_authenticated:
        return {}

    return {
        'PUSHER_KEY': settings.PUSHER_KEY,
        'PUSHER_USER_ID': user.id,
        'PUSHER_CLUSTER': getattr(settings, 'PUSHER_CLUSTER', 'us-east-1'),
        'csrf_token': context['csrf_token']
    }
