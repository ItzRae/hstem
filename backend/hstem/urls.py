from django.urls import path
from .views import AuthorList, CreatesList, ProjectList, FileList


urlpatterns = [
    path("authors/", AuthorList.as_view()),
    path("details/", CreatesList.as_view(), name="creates_list"),
    path("projects/", ProjectList.as_view(), name="project_list"),
    path("files/", FileList.as_view(), name="file_list"),

]
