from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, EventViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/organization/', OrganizationViewSet.as_view(), name='organization_view')
]
