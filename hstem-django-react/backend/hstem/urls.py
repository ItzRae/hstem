from django.urls import path
from . import views
from .views import create_author_project_relation

urlpatterns = [
  path('', views.hstem, name='hstem'),
  path('create_relation/<char:name>/<char:title>/', create_author_project_relation, name='create_relation'),
]


