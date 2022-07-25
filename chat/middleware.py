from django.contrib.auth.models import AnonymousUser
from knox.models import AuthToken
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware


@database_sync_to_async
def get_user(token):
    try:
        token_i = AuthToken.objects.get(token_key=token)
        return token_i.user
    except AuthToken.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        try:
            token = [
                x[1].decode().replace("Token ", "")
                for x in scope["headers"]
                if x[0].decode() == "authorization"
            ][0]
        except IndexError:
            token = None
        if token is None:
            scope["user"] = AnonymousUser()
        else:
            scope["user"] = await get_user(token)
        return await super().__call__(scope, receive, send)
