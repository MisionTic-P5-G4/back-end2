from django.contrib             import admin
from django.urls                import path
from rest_framework_simplejwt   import (TokenObtainPairView, TokenRefreshView)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from guarauthApp                import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view())
]
