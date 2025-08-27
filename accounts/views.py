from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django.contrib.auth import get_user_model, authenticate
from .models import Partner, Team, Portfolio
from .serializers import PartnerSerializer, TeamSerializer, PortfolioSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)





class UserListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            users = User.objects.all()
        else:
            users = User.objects.filter(id=request.user.id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_staff:
            return Response(
                {"error": "Faqat admin foydalanuvchi yaratishi mumkin"}, status=status.HTTP_403_FORBIDDEN
            )
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk, request):
        try:
            user = User.objects.get(pk=pk)

            if request.user.is_staff or user == request.user:
                return user
            return None
        except User.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_object(pk, request)
        if not user:
            return Response({"error": "Ruxsat yuq yoki user topilmadi"},status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk, request)
        if not user:
            return Response({"error": "Ruxsat yuq yoki user topilmadi"},status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk, request)
        if not user:
            return Response({"error": "Ruxsat yuq yoki user topilmadi"},status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"message": "User o‘chirildi"},status=status.HTTP_204_NO_CONTENT)



class PartnerCreateView(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, is_approved=False)


class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PortfolioListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
