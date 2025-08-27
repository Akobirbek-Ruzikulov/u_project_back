
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('', include('accounts.urls')),
        path('' ,include('news.urls')),
        path('', include('course.urls')),
    ]))
]
