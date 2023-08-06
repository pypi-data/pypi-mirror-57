from django.urls import path

from .views import pusher_auth


urlpatterns = [
    path('pusher/auth', pusher_auth, name='pusher_auth')
]
