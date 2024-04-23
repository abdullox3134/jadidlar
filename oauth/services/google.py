from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from oauth import serializer
from google.oauth2 import id_token # type: ignore
from google.auth.transport import requests # type: ignore
from users.models import CustomUser
from . import base_auth


def check_google_auth(google_user: serializer.GoogleAuth) -> dict:
    try:
        id_token.verify_oauth2_token(
            google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID
        )
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    user, _ = CustomUser.objects.get_or_create(email=google_user['email'])
    return base_auth.create_token(user.id)