from rest_framework.viewsets import ModelViewSet
from partners.models import Partner
from partners.serializers import PartnerSerializer
from accounts.permissions import IsAdminOrReadOnly


class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAdminOrReadOnly]