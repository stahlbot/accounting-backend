from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, RefreshToken
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

# from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Client

# Overwrite simple jwt ObtainPairSerializer to include the id and name of the user after authentication
class MyTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        # include name and id
        data['username'] = self.user.username
        data['id'] = self.user.id

        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'bio', 'profile_pic')
        read_only_fields = ('username', )

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'number', 'created_at', 'clerk')