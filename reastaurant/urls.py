from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet, basename='menu')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
]
