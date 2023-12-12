from django.urls import path
from . import views
from .views import create_author_project_relation

urlpatterns = [
  path('', views.hstem, name='hstem'),
  path('create_relation/<str:name>/<str:title>/', create_author_project_relation, name='create_relation'),
  # path('', views.upload_and_display_files, name='upload_and_display'),
]


