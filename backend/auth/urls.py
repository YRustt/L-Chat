from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path("obtain/", obtain_jwt_token),
    path("refresh/", refresh_jwt_token)
]
