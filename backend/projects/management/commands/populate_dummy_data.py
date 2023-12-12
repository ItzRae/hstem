from django.core.management.base import BaseCommand
from projects.models import Project
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = "Populate the database with dummy data"

    def handle(self, *args, **kwargs):
        Project.objects.all().delete()  # Clear existing data

        for _ in range(10):
            Project.objects.create(
                imageUrl="https://placekitten.com/300/200",
                title=fake.word(),
                author=fake.name(),
                date=fake.date_this_decade(),
                extension=fake.file_extension(),  # Provide a value for extension
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with dummy data"))
