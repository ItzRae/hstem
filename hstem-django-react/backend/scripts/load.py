import csv
import os 
from hstem.models import Author, Project, Create, File, Department, Sponsor

def run():
    file = open("./scripts/all_hstem_projects.csv", "r")
    read_file = csv.reader(file)

    Author.objects.all().delete()
    Project.objects.all().delete()
    Department.objects.all().delete()
    File.objects.all().delete()


    for row in read_file:
        print(row)
        name = row[1] + " " + row[2]
        a, created = Author.objects.get_or_create(name=name, major=row[3], year=row[4])
        p, created = Project.objects.get_or_create(title=row[5])
        
        a.save()
        p.save()


       


