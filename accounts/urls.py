from django.urls import path
from .views import UserListCreateView, UserDetailView, PartnerCreateView, TeamListCreateView, PortfolioListCreateView, \
    RegisterView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # JWT token olish
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # users
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    # login
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),

    path('partners/', PartnerCreateView.as_view(), name='partner-create'),
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('portfolio/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),

]
