# Generated by Django 5.0.6 on 2024-05-27 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lojista_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Produto",
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
                ("preco", models.DecimalField(decimal_places=2, max_digits=10)),
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
                ("estoque", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Foto",
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
                ("imagem", models.ImageField(upload_to="fotos_produtos/")),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fotos",
                        to="lojista_app.produto",
                    ),
                ),
            ],
        ),
    ]
