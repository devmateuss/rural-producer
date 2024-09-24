from decimal import Decimal
from typing import List

from pydantic import BaseModel


class FarmDTO(BaseModel):
    name: str
    city: str
    state: str
    total_area: Decimal
    agricultural_area: Decimal
    vegetation_area: Decimal
    planted_crops: List[str]
