import jwt
from django.conf import settings
from users.models import User


class JWTMiddelware(object):
    def resolve(self, next, root, info, **args):
        request = info.context
        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithm="HS256")
                pk = decoded.get("pk")
                user = User.objects.get(pk=pk)
                info.context.user = user
            except Exception:
                pass
        return next(root, info, **args)
