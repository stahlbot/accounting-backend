from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import AccountChart, User, Client
from .serializers import AccountChartSerializer, UserSerializer, ClientSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     serializer = self.serializer_class(data=request.data)

    #     if serializer.is_valid():
    #         print(serializer.data)
    #     else:
    #         print(serializer.errors)


class AccountChartViewSet(viewsets.ModelViewSet):
    queryset = AccountChart.objects.all()
    serializer_class = AccountChartSerializer

    @action(detail=False, methods=['GET'])
    def templates(self, request):
        templates = self.queryset.filter(is_template=True)
        serializer = self.get_serializer(templates, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def client_account_chart(self, request, pk=None):
        account_chart = self.get_object()
        if not account_chart.is_template and account_chart.client:
            serializer = self.get_serializer(account_chart.client)
            return Response(serializer.data)
        return Response(status=404)



# class UserLogIn(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token = Token.objects.get(user=user)
#         return Response({
#             'token': token.key,
#             'id': user.pk,
#             'username': user.username
#         })