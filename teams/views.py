from rest_framework.viewsets import ModelViewSet
from accounts.permissions import IsAdminOrReadOnly
from teams.models import Team
from teams.serializers import TeamSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminOrReadOnly]