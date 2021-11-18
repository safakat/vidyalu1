
from channels.db import database_sync_to_async

from urllib.parse import parse_qs

from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
import jwt
from django.conf import settings
from jwt import decode as jwt_decode
from django.contrib.auth import get_user_model
from channels.auth import AuthMiddlewareStack

@database_sync_to_async
def get_user(scope):
    try:
        token_key = parse_qs(scope["query_string"].decode('utf-8'))["token"][0]
        # token_decode = jwt.decode(token_key,settings.SECRET_KEY,algorithms=["HS256"])
        # print(token_decode)
        # token = Token.objects.get(key = token_decode)
        decoded_data = jwt_decode(token_key, settings.SECRET_KEY, algorithms=["HS256"])
        user = get_user_model().objects.get(id=decoded_data["user_id"])
        return user
    # except Token.DoesNotExist:
    #     AnonymousUser()
    except KeyError:
        print("error")
        return AnonymousUser()

# class TokenAuthMiddleware:
#     def __init__(self,inner):
#         self.inner = inner

#     def __call__(self,scope):
#         return TokenAuthMiddlewareInstance(scope,self)

# class TokenAuthMiddlewareInstance:
#     def __init__(self,scope,middleware):
#         self.scope = dict(scope)
#         self.inner = middleware.inner
    
#     async def __call__(self, receive, send):
#         self.scope['user'] = await get_user(self.scope)
#         inner = self.inner(self.scope)
#         return await inner(receive, send)

class QueryAuthMiddleware:
    def __init__(self,app):
        self.app = app
    async def __call__(self,scope,receive,send):
        scope['user'] = await get_user(scope)
        return await self.app(scope,receive,send)
TokenAuthMiddlewareStack = lambda inner:QueryAuthMiddleware(AuthMiddlewareStack(inner))

# from django.db import close_old_connections
# from rest_framework_simplejwt.tokens import UntypedToken
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from jwt import decode as jwt_decode
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from urllib.parse import parse_qs
# from channels.db import database_sync_to_async

# class TokenAuthMiddleware:
#     """
#     Custom token auth middleware
#     """

#     def __init__(self, inner):
#         # Store the ASGI application we were passed
#         self.inner = inner
    
#     async def __call__(self, scope):

#         # Close old database connections to prevent usage of timed out connections
#         close_old_connections()

#         # Get the token
#         print(scope["query_string"])
#         token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]

#         # Try to authenticate the user
#         try:
#             # This will automatically validate the token and raise an error if token is invalid
#             UntypedToken(token)
#         except (InvalidToken, TokenError) as e:
#             # Token is invalid
#             print(e)
#             return None
#         else:
#             #  Then token is valid, decode it
#             decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#             print(decoded_data)
#             # Will return a dictionary like -
#             # {
#             #     "token_type": "access",
#             #     "exp": 1568770772,
#             #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
#             #     "user_id": 6
#             # }

#             # Get the user using ID
#             user = await get_user_model().objects.get(id=decoded_data["user_id"])

#         # Return the inner application directly and let it run everything else
#         return self.inner(dict(scope, user=user))