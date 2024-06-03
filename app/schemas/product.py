from pydantic.types import PositiveInt
from pydantic import BaseModel, Field


class Product(BaseModel):
    """
    Class contains required product details with validation
    """
    # id: PositiveInt = Field(default=..., title="Product ID")
    name: str = Field(default=..., title="Product ID", min_length=2, max_length=255)
    category: str = Field(default=..., title="Product Category", min_length=2, max_length=255)
    price: float = Field(default=..., title="Product Price", ge=0.0)