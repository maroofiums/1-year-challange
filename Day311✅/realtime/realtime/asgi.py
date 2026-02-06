import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),       # normal HTTP
    "websocket": URLRouter(websocket_urlpatterns),  # websocket
})
