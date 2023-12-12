# Generated by Django 4.2.7 on 2023-11-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imageUrl", models.URLField()),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("extension", models.CharField(default="", max_length=10)),
            ],
        ),
    ]
