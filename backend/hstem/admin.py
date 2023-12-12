from django.contrib import admin
from .models import Author, Creates, Project


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "major", "year")


class CreatesAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "created_at")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Creates, CreatesAdmin)
admin.site.register(Project, ProjectAdmin)

