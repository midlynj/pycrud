from rest_framework import serializers
from usersapimixin.models import User, UserDto


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDto
        fields = "__all__"
