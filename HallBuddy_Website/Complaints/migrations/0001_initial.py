# Generated by Django 5.0.2 on 2024-03-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Complaint_Request",
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
                ("User_Name", models.CharField(max_length=30)),
                ("location", models.TextField(default="Not Given", max_length=15)),
                ("Done", models.BooleanField(default=False)),
                ("Place", models.CharField(default="Not Given", max_length=10)),
                ("category", models.CharField(default="Not Given", max_length=20)),
                ("sub_category", models.CharField(default="Not Given", max_length=20)),
                ("comments", models.TextField(max_length=200)),
                ("Complaint_DateTime", models.DateTimeField()),
            ],
        ),
    ]