from django.contrib import admin
from accounts.models import User, Partner, Team, Portfolio

admin.site.register(User)
admin.site.register(Partner)
admin.site.register(Team)
admin.site.register(Portfolio)
