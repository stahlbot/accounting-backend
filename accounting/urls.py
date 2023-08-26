from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from api.views import AccountChartViewSet, AccountViewSet, BookingViewSet, CategoryViewSet, UserViewSet, ClientsViewSet, ClientAccountChartViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientsViewSet)
router.register(r'account-charts', AccountChartViewSet)
router.register(r'categories', CategoryViewSet)

# This router is not even used
# clients/:client_id/account-charts
client_account_charts_router = routers.NestedSimpleRouter(router, r'clients', lookup='client')
client_account_charts_router.register(r'account-charts', ClientAccountChartViewSet, basename='client-account-charts')

# account-charts/:account_chart_id/accounts
account_chart_accounts_router = routers.NestedSimpleRouter(router, r'account-charts', lookup='accountchart')
account_chart_accounts_router.register(r'accounts', AccountViewSet, basename='account-chart-accounts')

# clients/:client_id/bookings
client_bookings_router = routers.NestedSimpleRouter(router, r"clients", lookup="client")
client_bookings_router.register(r'bookings', BookingViewSet, basename="client-bookings")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(client_account_charts_router.urls)),
    path('api/v1/', include(account_chart_accounts_router.urls)),
    path('api/v1/', include(client_bookings_router.urls)),
    # path('api-user-login/', UserLogIn.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # URL for JWT token authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)