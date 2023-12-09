from django.shortcuts import render
from .models import Author, Create, Project

# Create your views here.

from django.shortcuts import render
from .services import get_all_rows

def hstem(request):
  names = get_all_rows("hstem test")
  return render(request, 'hstem.html', {'names': names})

def create_author_project_relation(request, name, title):
    # Assuming you have author_id and project_id passed to the function

    # Retrieve the specific author and project from the database
    author = Author.objects.get(id=name)
    project = Project.objects.get(id=title)

    # Creating a Create relationship
    create_relationship = Create(author=author, project=project, role="Writer")
    create_relationship.save()

    # Return a response, for example, redirect to a new page or render a template
    return render(request, 'some_template.html', {'message': 'Relationship created'})



