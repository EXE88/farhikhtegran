from django.urls import path
from .views import *

urlpatterns = [
    path("verifytokens/",VerifyTokens.as_view(),name="user_token_verify"),
]
