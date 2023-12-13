import csv
import os 
from hstem.models import Author, Project, Create, File
from django.utils import timezone

def run():
    file = open("/Users/rachellin/Desktop/hstemdb/hstem-django-react/backend/scripts/hstemprojects.csv", "r")
    read_file = csv.reader(file)


    Create.objects.all().delete()
    File.objects.all().delete()
    Author.objects.all().delete()
    Project.objects.all().delete()


    # Department.objects.all().delete()
    # File.objects.all().delete()


    for row in read_file:
        print(row)
        name = row[1] + " " + row[2]
        a, _ = Author.objects.get_or_create(name=name, major=row[3], year=row[4])
        p, _ = Project.objects.get_or_create(title=row[5], cohort=row[0], description=row[10], audience=Project.Audience.STUDENTS)
        c, _ = Create.objects.get_or_create(name=a, title=p, created_at=timezone.now())
        f, _ = File.objects.get_or_create(name=name, type=File.FileType.OTHER, title=p, file=row[8])

        
        a.save()
        p.save()
        c.save()
        f.save() 


       


