from django.urls import path

from notification.notification_consumers import NotificationConsumer

websocket_urlpatterns = [
    path('live_notification/', NotificationConsumer.as_asgi()),
]