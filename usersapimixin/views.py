from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from usersapimixin.UserSerializer import UserDtoSerializer, UserSerializer
from usersapimixin.models import User, UserDto


class UserMixinList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # checking authentication

    def get(self, request, *args, **kwargs):
        """Get user details"""
        try:
            instance = User.objects.get(pk=kwargs['pk'])
            instance.status = instance.status_display

        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(instance)
        return Response(serializer.data)


class UserDelete(APIView):
    def delete(self, request, *args, **kwargs):
        try:
            instance = User.objects.get(pk=kwargs['pk'])

        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)


class UserUpdate(APIView):
    def put(self, request, *args, **kwargs):
        """Update User"""
        try:
            instance = User.objects.get(pk=kwargs['pk'])

        except User.DoesNotExist:
            raise Http404

        serializer = UserSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(APIView):
    def post(self, request, *args, **kwargs):
        # try:
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserMixinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        """Overriding destroy method to change status to inactive"""
        try:
            instance = self.get_queryset().get(pk=kwargs['pk'])
            print(instance.status)

        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        instance.status = 2
        instance.save()
        serializer = UserSerializer(instance)
        return Response(serializer.data)


class UserDtoDetail(APIView):

    def get(self, request, *args, **kwargs):
        """Return dto of User"""
        try:
            instance = User.objects.get(pk=kwargs['pk'])
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user_dto = UserDto()
        user_dto.first_name = instance.first_name
        user_dto.id = instance.id

        serializer = UserDtoSerializer(user_dto)

        return Response(serializer.data)
