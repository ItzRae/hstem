from django.db import models

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
    audience = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Create(models.Model):
    date = models.DateField()
    name = models.ForeignKey(Author, primary_key=True, on_delete=models.DO_NOTHING) # on delete no action
    title = models.ForeignKey(Project, on_delete=models.DO_NOTHING) # on delete no action

    
class File(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    is_public = models.BooleanField()
    type = models.CharField(max_length=50)
    title = models.ForeignKey(Project, on_delete=models.DO_NOTHING) # on delete no action

    def __str__(self):
        return (self.title, self.name, self.type)
    
class Department(models.Model):
    school = models.CharField(primary_key=True, max_length=100)

class Sponsor(models.Model):
    title = models.ForeignKey(Project, on_delete=models.DO_NOTHING) # on delete no action
    school = models.ForeignKey(Department, primary_key=True, on_delete=models.DO_NOTHING) # on delete no action

    def __str__(self):
        return (self.school, self.title)


