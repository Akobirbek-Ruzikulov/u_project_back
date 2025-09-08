from django.contrib import admin
from teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'exp', 'is_active', 'created_at')
    search_fields = ('name', 'position')