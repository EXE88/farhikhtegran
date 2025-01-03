from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/" , include("users.urls")),
    path("scores/",include("scores.urls")),
    path("homeworks/",include("homeworks.urls")),
    path("attendance/",include("attendance.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('comment/',include("comments.urls")),
]
