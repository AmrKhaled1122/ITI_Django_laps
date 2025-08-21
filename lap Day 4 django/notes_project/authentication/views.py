from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
