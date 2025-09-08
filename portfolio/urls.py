from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from portfolio.views import PortfolioViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')

urlpatterns = [
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)