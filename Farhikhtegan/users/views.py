from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import AllUsersMetaData , TeachersMetaData , StudentsMetaData

class VerifyTokens(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self,request):
        return Response({"valid":True},200)
    
class GetUserInfo(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        user_User_class = User.objects.get(id=request.user.id)
        user_AllUsersMetaData_class = AllUsersMetaData.objects.get(user=request.user)

        if user_AllUsersMetaData_class.is_teacher:
            data = {
                "user_id":request.user.id,
                "is_teacher":user_AllUsersMetaData_class.is_teacher,
                "username":user_User_class.username,
                "first_name":user_AllUsersMetaData_class.first_name,
                "last_name":user_AllUsersMetaData_class.last_name,
                "age":user_AllUsersMetaData_class.age,
                "national_code":user_User_class.username,
                "lessons":[lesson.name for lesson in TeachersMetaData.objects.get(user=request.user).lessons.all()]
            }
        else:
            data = {
                "user_id":request.user.id,
                "is_teacher":user_AllUsersMetaData_class.is_teacher,
                "username":user_User_class.username,
                "first_name":user_AllUsersMetaData_class.first_name,
                "last_name":user_AllUsersMetaData_class.last_name,
                "age":user_AllUsersMetaData_class.age,
                "national_code":user_User_class.username,
                "grade":next((name for key, name in StudentsMetaData.GRADE_CHOICES if key == StudentsMetaData.objects.get(user=request.user).grade), None),
                "subject":next((name for key, name in StudentsMetaData.SUBJECT_CHOICES if key == StudentsMetaData.objects.get(user=request.user).subject), None),
                "school_class":user_User_class.groups.all()[0].name
            } 
        return Response(data,200)