from django.shortcuts import render
from rest_framework import viewsets, generics

from usersapi.UserSerializer import UserSerializer
from usersapi.models import User

# Create your views here.
"""Full crud"""


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
