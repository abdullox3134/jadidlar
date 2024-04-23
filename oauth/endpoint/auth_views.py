from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .. import serializer
from ..services import google


@api_view(["POST"])
def google_auth(request):
    """ Подтверждение авторизации через Google
    """
    google_data = serializer.GoogleAuth(data=request.data)
    if google_data.is_valid():
        token = google.check_google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')


# @api_view(["POST"])
# def google_auth(request):
#     """ Подтверждение авторизации через Google
#     """
#     # Serializer ni yaratish va tekshirish
#     google_data = serializer.GoogleAuth(data=request.data)
#     if google_data.is_valid():
#         # Serializer ma'lumotlarni olish
#         data = google_data.validated_data
#         # Google autentifikatsiyasini tekshirish va token olish
#         token = google.check_google_auth(data)
#         # Tokenni qaytarish
#         return Response({"token": token})
#     else:
#         # Agar serializer ma'lumotlarni qabul qilmagan bo'lsa
#         raise AuthenticationFailed(detail='Bad data Google')

