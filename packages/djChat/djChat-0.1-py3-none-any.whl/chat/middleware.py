from http import cookies

from channels.auth import AuthMiddlewareStack
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from rest_framework_simplejwt.authentication import JWTAuthentication


class JsonWebTokenAuthenticationFromScope(JWTAuthentication):
    """
    Extracts the JWT from a channel scope (instead of an http request)
    """

    def authenticate(self, scope):
        try:
            cookie = next(x for x in scope['headers'] if x[0].decode('utf-8') == 'cookie')[
                1
            ].decode('utf-8')
            header = cookies.SimpleCookie(cookie)['X-Authorization'].value
        except:
            return None

        if header is None:
            return None

        raw_token = self.get_raw_token(f'Bearer {header}'.encode())
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token


class JsonTokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):

        try:
            # Close old database connections to prevent usage of timed out connections
            close_old_connections()
            adapter = JsonWebTokenAuthenticationFromScope()
            user, jwt_value = adapter.authenticate(scope)
            scope['user'] = user
        except:
            scope['user'] = AnonymousUser()

        return self.inner(scope)


def JsonTokenAuthMiddlewareStack(inner):
    return JsonTokenAuthMiddleware(AuthMiddlewareStack(inner))
