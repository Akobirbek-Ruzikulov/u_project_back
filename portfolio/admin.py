from django.contrib import admin
from portfolio.models import Portfolio



@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'url_link', 'is_active', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('is_active', 'created_at')