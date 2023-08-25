from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, RefreshToken
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

# from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Account, AccountChart, Category, User, Client

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
        fields = ('id', 'username', 'first_name', 'last_name', 'bio', 'profile_pic', 'email')
        read_only_fields = ('username', )

class ClientSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(source='created_at', required=False)
    # accountChart = serializers.PrimaryKeyRelatedField(source="accountchart.id", queryset=Client.objects.all())
    class Meta:
        model = Client
        fields = ('id', 'name', 'number', 'createdAt', 'clerk')
        # read_only_fields = ('created_at',)


class AccountChartSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), allow_null=True)
    isTemplate = serializers.BooleanField(source='is_template')

    class Meta:
        model = AccountChart
        fields = ('id', 'name', 'isTemplate', 'client')


class AccountSerializer(serializers.ModelSerializer):
    accountChart = serializers.PrimaryKeyRelatedField(queryset=AccountChart.objects.all(), source='account_chart')
    nonDeductibleTax = serializers.BooleanField(source='non_deductible_tax')

    class Meta:
        model = Account
        fields = ('id', 'name', 'number', 'nonDeductibleTax', 'accountChart', 'category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'document')


# class OptionalPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
#     def to_internal_value(self, data):
#         if data in serializers.Empty:
#             return None
#         return super().to_internal_value(data)

# class AccountChartSerializer(serializers.ModelSerializer):
#     client = OptionalPrimaryKeyRelatedField(queryset=Client.objects.all(), required=False, allow_null=True)

#     class Meta:
#         model = AccountChart
#         fields = '__all__'

#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         print(ret)
#         if ret.get('client') is None:
#             ret['client'] = None
#         return ret