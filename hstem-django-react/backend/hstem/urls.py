from django.urls import path
from . import views
from .views import create_author_project_relation

urlpatterns = [
  path('', views.hstem, name='hstem'),
  path('create_relation/<int:author_id>/<int:project_id>/', create_author_project_relation, name='create_relation'),
]


