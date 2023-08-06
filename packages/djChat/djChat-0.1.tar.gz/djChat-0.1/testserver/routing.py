from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing
from chat.middleware import JsonTokenAuthMiddlewareStack

application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
        'websocket': JsonTokenAuthMiddlewareStack(
            URLRouter(chat.routing.websocket_urlpatterns)
        ),
    }
)
