import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import products.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        products.routing.websocket_urlpatterns
    ),
})

