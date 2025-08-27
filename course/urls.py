from django.urls import path
from .views import CategoryListCreateUpdateView

urlpatterns = [
    path('categories/', CategoryListCreateUpdateView.as_view(), name='category-list-create'),
]
