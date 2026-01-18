from django.urls import path
from .api_views import signup_api, login_api

urlpatterns = [
    path('api/signup/', signup_api, name='signup_api'),
    path('api/login/', login_api, name='login_api'),
]

