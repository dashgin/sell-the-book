from allauth.account import adapter
from dj_rest_auth.serializers import (
    LoginSerializer as RestAuthLoginSerializer,
    UserDetailsSerializer as RestAuthUserDetailsSerializer
)
from dj_rest_auth.registration.serializers import RegisterSerializer as RestAuthRegisterSerializer
from rest_framework import serializers

from accounts.models import CustomUser


class LoginSerializer(RestAuthLoginSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    username = None


class RegisterSerializer(RestAuthRegisterSerializer):
    full_name = serializers.CharField(max_length=200)


    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    username = None


class UserDetailsSerializer(RestAuthUserDetailsSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'email', 'full_name')
        read_only_fields = ('email',)