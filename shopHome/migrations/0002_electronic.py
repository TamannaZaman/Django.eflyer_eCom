# Generated by Django 4.1.7 on 2023-03-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopHome", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Electronic",
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
                ("name", models.CharField(max_length=250)),
                ("price", models.FloatField()),
                ("image", models.ImageField(upload_to="images")),
            ],
        ),
    ]
