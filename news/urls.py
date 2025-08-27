from django.urls import path
from .views import NewsListCreateView, NewsDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('news/', NewsListCreateView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)