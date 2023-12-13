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
    description = models.CharField(max_length=5000)
    cohort = models.CharField(max_length=100)
    
    # STUDENTS = 'Students'
    # AUDIENCE_CHOICES = (
    #     (STUDENTS, 'Students'),
    # )

    class Audience(models.TextChoices):
        STUDENTS = 'students', 'Students'
        FACULTY = 'faculty', 'Faculty'
        FIVE_C = '5c', '5C'
        OTHER = 'other', 'Other'
    audience = models.CharField(max_length=100, choices=Audience.choices, default=Audience.STUDENTS)


    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Create(models.Model):
    title = models.ForeignKey(Project, on_delete=models.DO_NOTHING, db_column='title') # on delete no action
    name = models.ForeignKey(Author, primary_key=True, on_delete=models.DO_NOTHING, db_column='name') # on delete no action
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.name, self.title, self.created_at)
    
class File(models.Model):
    name = models.CharField(primary_key=True, max_length=100, db_column='name')
    is_public = models.BooleanField(default=True)

    class FileType(models.TextChoices):
        IMAGE = 'img','Image'
        VIDEO = 'mp3', 'Video'
        AUDIO = 'mp4', 'Audio'
        PDF = 'pdf', 'PDF'
        PPT = 'ppt', 'Powerpoint'
        OTHER = 'other','Other'
    
    type = models.CharField(max_length=50, choices=FileType.choices, default=FileType.OTHER)
    title = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=False, db_column='title') # on delete no action
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=False, null=True)


    