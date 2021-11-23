"""casedomain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt import serializers as jwt_serializers

from casedomain import views

router = routers.DefaultRouter()

class TokenObtainPairPatchedSerializer(jwt_serializers.TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = {
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,

        }

        data['token'] = data['access']

        return data


class TokenObtainPairPatchedView(jwt_views.TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairPatchedSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth-user/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api-auth-user/change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='api_auth_change_password'),
    path('api/v2/token/', TokenObtainPairPatchedView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v2/num_to_english/', views.NumberConverterView.as_view(), name='num_to_english')
]
