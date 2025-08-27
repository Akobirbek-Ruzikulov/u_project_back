from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateUpdateView(generics.ListCreateAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.prefetch_related('subcategories__prices').all()

    def get_permissions(self):
        user = self.request.user
        if user.is_staff:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({"detail": "Sizda ruxsat yo‘q"}, status=403)
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({"detail": "Sizda ruxsat yo‘q"}, status=403)
        return super().put(request, *args, **kwargs)
