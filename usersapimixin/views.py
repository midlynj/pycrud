from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import generics

from usersapimixin.UserSerializer import UserSerializer
from usersapimixin.models import User

"""Inheritance from mixin crud methods"""


class UserMixinList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMixinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def getr(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
