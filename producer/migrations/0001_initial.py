# Generated by Django 5.1.1 on 2024-09-25 12:37

from django.db import migrations, models

import producer.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Producer",
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
                    "document",
                    models.CharField(
                        max_length=14,
                        unique=True,
                        validators=[producer.validators.validate_document],
                        verbose_name="CPF or CNPJ",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Name of Producer"),
                ),
            ],
        ),
    ]
