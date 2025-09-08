from rest_framework.viewsets import ModelViewSet
from portfolio.models import Portfolio
from portfolio.serializers import PortfolioSerializer
from accounts.permissions import IsAdminOrReadOnly


class PortfolioViewSet(ModelViewSet):
    queryset = Portfolio.objects.select_related('partner').all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAdminOrReadOnly]