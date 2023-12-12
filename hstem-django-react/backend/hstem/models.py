from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length=1000)
    primary_theme = models.CharField(max_length=100)
    secondary_theme = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/', blank=False, null=True)
    
    # STUDENTS = 'Students'
    # AUDIENCE_CHOICES = (
    #     (STUDENTS, 'Students'),
    # )
    audience = models.CharField(max_length=100)


    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Create(models.Model):
    name_id = models.ForeignKey(Author, primary_key=True, on_delete=models.DO_NOTHING) # on delete no action
    title_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING) # on delete no action
    created_at = models.DateTimeField(default=timezone.now)

    
# class File(models.Model):
#     name = models.CharField(primary_key=True, max_length=100)
#     is_public = models.BooleanField(default=False)
#     type = models.CharField(max_length=50)
#     title = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=False) # on delete no action
#     uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

#     def __str__(self):
#         return (self.title, self.name, self.type)
    