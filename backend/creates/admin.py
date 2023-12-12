from django.contrib import admin
from .models import Creates


class CreatesAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "created_at")


admin.site.register(Creates, CreatesAdmin)
