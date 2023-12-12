from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "major", "year")


admin.site.register(Author, AuthorAdmin)