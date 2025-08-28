
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_views = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_views.with_ui('swagger',
                                          cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_views.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('', include('accounts.urls')),
        path('' ,include('news.urls')),
        path('', include('course.urls')),
    ]))
]
