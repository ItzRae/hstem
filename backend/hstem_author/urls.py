from django.urls import path
from .views import HstemAuthorList

urlpatterns = [
    path('hstem_authors/', HstemAuthorList.as_view(), name='hstem_author_list'),
]