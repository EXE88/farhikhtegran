from django.urls import path
from .views import *

urlpatterns = [
    path("getuser/",GetUser.as_view(),name="get_user"),
]
