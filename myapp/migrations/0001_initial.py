# Generated by Django 4.1 on 2023-01-04 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="contactinfo",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("subject", models.CharField(max_length=100)),
                ("message", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="journeyDetails",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("dayid", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=150)),
                ("hall", models.CharField(max_length=100)),
                ("date", models.DateField(max_length=100)),
                ("time", models.TimeField(max_length=100)),
                ("comtime", models.DateTimeField(max_length=100)),
                ("Blocation", models.CharField(max_length=100)),
                ("Dlocation", models.CharField(max_length=100)),
                ("cityfrom", models.CharField(max_length=100)),
                ("cityto", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                (
                    "comments",
                    models.CharField(
                        default=datetime.datetime.today, max_length=100, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Loggedin",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("loggedin", models.CharField(max_length=100)),
                ("time", models.TimeField(max_length=100)),
                ("date", models.DateField(max_length=100)),
            ],
        ),
    ]
