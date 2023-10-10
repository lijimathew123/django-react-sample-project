
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import UserProfile
from .serializers import UserSerializer,UserProfileSerializer

from rest_framework.authtoken.models import Token


def index(request):
    return render(request,'index.html')





# /////////////////////////////////////////////register logic here/////////////////////////////////////

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        print("User details received:", request.data)   # ////////////////////////Debugging purpose/////////////////////////////
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            # Create a UserProfile instance for the user
            UserProfile.objects.create(user=user)

            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Serializer is invalid', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"Logged-in User: {user.username}")  #////////////////////////////// For debugging code
             # Create or retrieve a token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'Login successful','token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile)
        print(f"profile details : {serializer.data}")
        return Response(serializer.data, status=200)
    except UserProfile.DoesNotExist:
        return Response({'message': 'Profile not found'}, status=404)
   
    
