from django.contrib import admin
from .models import HstemAuthor

class HstemAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'major', 'year')

admin.site.register(HstemAuthor, HstemAuthorAdmin)