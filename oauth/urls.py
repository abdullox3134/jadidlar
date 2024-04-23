from django.urls import path
from .endpoint import  auth_views

urlpatterns = [

    path('google/', auth_views.google_auth),

]