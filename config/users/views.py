from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListView(APIView):
    def get(self, request):
        return Response({"message": "Hello Users"})

# Create your views here.

from .serializers import SignUpSerializer
from .services import UserService

class SignUpView(APIView):
    def post(self,request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserService.signup(serializer.validated_data)

        return Response({"message": "User created successfully." ,"status": status.HTTP_201_CREATED})