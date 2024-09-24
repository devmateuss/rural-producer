from farm.schema import FarmDTO


def validate_area(farm: FarmDTO) -> ValueError | None:
    if farm.agricultural_area + farm.vegetation_area > farm.total_area:
        raise ValueError(
            "A soma da área agricultável e vegetação não pode exceder a área total."
        )
