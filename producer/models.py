from django.db import models

from producer.validators import validate_document


class Producer(models.Model):
    document = models.CharField(
        "CPF or CNPJ",
        max_length=14,
        unique=True,
        null=False,
        validators=[validate_document],
    )
    name = models.CharField("Name of Producer", max_length=150)
