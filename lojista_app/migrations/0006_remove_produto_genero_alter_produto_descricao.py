# Generated by Django 4.2.13 on 2024-05-28 03:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lojista_app", "0005_produto_genero"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produto",
            name="genero",
        ),
        migrations.AlterField(
            model_name="produto",
            name="descricao",
            field=ckeditor.fields.RichTextField(),
        ),
    ]