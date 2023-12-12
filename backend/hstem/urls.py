from django.urls import path
from .views import AuthorList


urlpatterns = [
    path("authors/", AuthorList.as_view(), name="author_list"),
]
