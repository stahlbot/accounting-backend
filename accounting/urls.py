from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from api.views import AccountChartViewSet, UserViewSet, ClientsViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientsViewSet)
router.register(r'account-charts', AccountChartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api-user-login/', UserLogIn.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # URL for JWT token authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)