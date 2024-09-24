from django.db import models

from producer.models import Producer

PLANTED_CROPS_CHOICES = {
    "AÇUCAR": "SUGGAR",
    "MILHO": "CORN",
    "ALGODÂO": "COTTON",
    "CAFÉ": "COFFEE",
    "CANA DE AÇUCAR": "SUGGAR CANE",
    "SOJA": "SOY",
}


class Farm(models.Model):
    producer = models.ForeignKey(
        Producer, on_delete=models.CASCADE, related_name="producer_farm"
    )
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    total_area = models.DecimalField(max_digits=10, decimal_places=3)
    agricultural_area = models.DecimalField(max_digits=10, decimal_places=3)
    vegetation_area = models.DecimalField(max_digits=10, decimal_places=3)
    planted_crops = models.ManyToManyField("Crop", related_name="farms")


class Crop(models.Model):
    name = models.CharField(choices=PLANTED_CROPS_CHOICES)
