from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UsersMetaData


class GetUser(APIView):
    #TODO:return valuev of all the fields that exists in model
    def get(self,request):
        user_details = UsersMetaData.objects.get(user=request.user)
        content = {
            "message":"successfull",
            "id":request.user.id,
            "username":request.user.username,
            "first name":user_details.first_name,
            "last name":user_details.last_name,
            "age":user_details.age,
            "is teacher":user_details.is_teacher,
            "lessons":user_details.lessons.all().values("name"),
            "available subjects":user_details.SUBJECT_CHOICES,
            "subject":user_details.subject
        }
        return Response(content)