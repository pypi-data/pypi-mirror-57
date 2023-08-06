from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse

from .utils import get_pusher_client


@login_required
def pusher_auth(request):
    """Authenticate private user channel."""
    channel = request.POST['channel_name']

    user_id = int(channel.split('-')[-1])

    if user_id != request.user.id:
        return HttpResponseForbidden()

    pusher_client = get_pusher_client()
    payload = pusher_client.authenticate(
        channel=channel,
        socket_id=request.POST['socket_id']
    )

    return JsonResponse(payload)
