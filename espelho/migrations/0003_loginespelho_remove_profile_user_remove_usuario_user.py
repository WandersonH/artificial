# Generated by Django 5.0.6 on 2024-05-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("espelho", "0002_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoginEspelho",
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
                ("data_login", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="user",
        ),
    ]
