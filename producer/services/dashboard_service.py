from django.db import models

from farm.models import Farm


class DashboardService:
    @staticmethod
    def get_farm_stats():
        total_farms = Farm.objects.count()
        total_hectares = Farm.objects.aggregate(total_area=models.Sum("total_area"))[
            "total_area"
        ]
        state_distribution = Farm.objects.values("state").annotate(
            count=models.Count("id")
        )
        crop_distribution = (
            Farm.objects.values(crop_name=models.F("planted_crops__name"))
            .annotate(count=models.Count("planted_crops"))
            .order_by("planted_crops")
        )
        land_use = Farm.objects.aggregate(
            total_agricultural_area=models.Sum("agricultural_area"),
            total_vegetation_area=models.Sum("vegetation_area"),
        )

        return {
            "total_farms": total_farms,
            "total_hectares": total_hectares,
            "state_distribution": state_distribution,
            "crop_distribution": crop_distribution,
            "land_use": land_use,
        }
