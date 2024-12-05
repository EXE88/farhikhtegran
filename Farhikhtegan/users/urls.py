from django.urls import path
from .views import *

#TODO:add more user needed url path
urlpatterns = [
    path("getuser/",GetUser.as_view(),name="get_user"),
]
