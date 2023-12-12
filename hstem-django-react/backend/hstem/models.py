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
    name = models.ForeignKey(Author, primary_key=True, on_delete=models.DO_NOTHING, db_column='name', default='Student') # on delete no action
    title = models.ForeignKey(Project, on_delete=models.DO_NOTHING, db_column='title', default="A Project") # on delete no action
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.name, self.title, self.created_at)
    
class File(models.Model):
    name = models.CharField(primary_key=True, max_length=100, db_column='name')
    is_public = models.BooleanField(default=False)
    type = models.CharField(max_length=50)
    title = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=False, db_column='title') # on delete no action
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=False, null=True)


    def __str__(self):
        return (self.title, self.name, self.type)
    