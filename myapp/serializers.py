from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = [ 'username', 'email','password']  



class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    password = serializers.CharField(source='user.password', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username','email','password']