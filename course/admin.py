from django.contrib import admin

from course.models import Category, SubCategory, Price

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Price)
