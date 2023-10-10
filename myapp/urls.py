
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('register/', views.register),
    path('login_view/', views.login_view),
   

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]
