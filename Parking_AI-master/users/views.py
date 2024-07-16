from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate 
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': 'user_token'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserView(APIView):
    def post(self, request,format=None ):
        print("Creating a User")

        user_data = request.data
        print(request.data)

        user_serializer = UserSerializer(user_data)
        if user_serializer.is_valid(raise_exception=False):
            user_serializer.save()
            return Response({"user": user_serializer.data},status = 200)
        
        return Response({"msg":"ERR"},status = 400)



class UserLoginView(APIView):
    def get(self , request ,format= None):
        if request.user.is_authenticate == False or request.user.is_inactive == False:
            return Response("Invalid credentials", status = 403)
        
            user = UserSerializer(request.user)

            return Response(user.data,status=200)
        
    def post(self, request ,formart = None):
        print("Login Class")
        user_obj= User.objects.filter(email = request.data['username']).first or User.objects.filter(username=request.data["username"]).first()
        if user_obj is not None:
            credentials= {
                'username':user_obj.username,
                'password':request.data['password']
            }
            user=authenticate(**credentials)

            if user and user.is_active:
                user_serializer = UserSerializer(user)

                return Response(user_serializer.data,status=200)
            
            return Response("invalid credentials" , status=403)