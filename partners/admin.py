from django.contrib import admin
from partners.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'is_approved', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('is_approved', 'created_at')