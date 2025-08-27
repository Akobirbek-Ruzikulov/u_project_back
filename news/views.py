from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import News
from .serializers import NewsSerializer
from .permissions import IsAdminOrReadOnly


class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]

