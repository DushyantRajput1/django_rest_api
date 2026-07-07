from logging import exception

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListView(APIView):
    def get(self, request):
        return Response({"message": "Hello Users"})

# Create your views here.

from .serializers import SignUpSerializer ,OTPVerificationSerializer , LOGINSerializer , UserSerializer
from .services import UserService ,  OTPVerificationService , LOGINService , UserServicelist
  
class SignUpView(APIView):
    def post(self,request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserService.signup(serializer.validated_data)

        return Response({"message": "User created successfully." ,"status": status.HTTP_201_CREATED})
    
class OTPVerificationView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        otp = serializer.validated_data["otp"]  
        is_verified, message = OTPVerificationService.verify_otp(email, otp)

        return Response({"message": message, "status": status.HTTP_200_OK} if is_verified else {"message": message, "status": status.HTTP_400_BAD_REQUEST})
    

class LOGINView(APIView):
    def post(self, request):
        serializer = LOGINSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        is_authenticated, message = LOGINService.login(email, password)

        return Response({"message": message, "status": status.HTTP_200_OK} if is_authenticated else {"message": message, "status": status.HTTP_400_BAD_REQUEST})


class UserListView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            try:
                user = UserServicelist.get_user_by_id(user_id)
                serializer = UserSerializer(user)
                if not user:
                    return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            except exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        users = UserServicelist.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)