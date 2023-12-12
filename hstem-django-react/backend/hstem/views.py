from django.shortcuts import render, redirect
from .models import Author, Create, Project
# from .models import File
# from .forms import UploadFileForm

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

# def upload_and_display_files(request):
#     files = File.objects.all()

#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             for file in request.FILES.getlist('files'):
#                 File.objects.create(file=file)
#             return redirect('upload_and_display')
#     else:
#         form = UploadFileForm()

#     return render(request, 'upload_and_display.html', {'form': form, 'files': files})

