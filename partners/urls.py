from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PartnerViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet, basename='partner')


urlpatterns = [
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)