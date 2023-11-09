import csv
import os 
from hstem.models import Author, Project, Create, File, Department, Sponsor

def run():
    file = open("/Users/rachellin/Desktop/hstemdb/hstem-django-react/backend/scripts/hstem short test.csv", "r")
    read_file = csv.reader(file)

    Author.objects.all().delete()
    Project.objects.all().delete()
    Department.objects.all().delete()
    File.objects.all().delete()
    


    count = 1

    for author in read_file:
        if count == 1:
            pass
        else:
            print(author)
            Author.objects.create(name=author[0], major=author[1], year=author[2])
        count += 1
