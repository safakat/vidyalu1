"""
ASGI config for vidyalu project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vidyalu.settings')
django.setup()

from django.core.asgi import get_asgi_application

from django.urls import path

from channels.auth import AuthMiddlewareStack

from channels.routing import ProtocolTypeRouter, URLRouter


from chat.custom_token_authentication import QueryAuthMiddleware

import chat.routing

import notification.routing


application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket":QueryAuthMiddleware(
        
        URLRouter(
            notification.routing.websocket_urlpatterns +
            chat.routing.websocket_urlpatterns
        )
    )
    
})

# application = ProtocolTypeRouter({
#     "http":get_asgi_application(),
#     "websocket":AuthMiddlewareStack(
#         URLRouter([
#             path('ws/chat/',EchoConsumer.as_asgi()),
#         ])
#     )
# })
