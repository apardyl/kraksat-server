"""kraksat_server URL Configuration"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from rest_framework import routers

from api.views import SHTViewSet, IMUViewSet, GPSViewSet, PhotoViewSet

router = routers.DefaultRouter()
router.register(r'sht', SHTViewSet)
router.register(r'imu', IMUViewSet)
router.register(r'gps', GPSViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)