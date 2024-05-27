# Generated by Django 5.0.6 on 2024-05-26 22:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProdutoLojista",
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
                ("nome", models.CharField(max_length=255)),
                ("descricao", models.TextField()),
                ("imagem", models.ImageField(upload_to="produtos/")),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("cores_disponiveis", models.CharField(max_length=255)),
                ("categoria", models.CharField(max_length=100)),
                ("quantidade_usos", models.PositiveIntegerField(default=0)),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                (
                    "estacao",
                    models.CharField(
                        choices=[
                            ("primavera", "Primavera"),
                            ("verao", "Verão"),
                            ("outono", "Outono"),
                            ("inverno", "Inverno"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "avatar",
                    models.ImageField(blank=True, null=True, upload_to="avatars/"),
                ),
                ("medidas", models.JSONField(blank=True, null=True)),
                ("preferencias_estilo", models.CharField(blank=True, max_length=100)),
                ("nome_loja", models.CharField(blank=True, max_length=255)),
                ("endereco", models.CharField(blank=True, max_length=255)),
                ("horario_funcionamento", models.CharField(blank=True, max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
