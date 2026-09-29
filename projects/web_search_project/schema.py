from pydantic import BaseModel, Field


class RestaurantInfo(BaseModel):
    name: str = Field(description="Name of the restaurant")
    location: str = Field(description="Exact location of the restaurant")
    description: str = Field(description="Description of the restaurant")
    phone_number: str | None = Field(
        default=None,
        description="Phone number of the restaurant"
    )
    special_thing: str | None = Field(
        default=None,
        description="What makes this restaurant special or unique"
    )
    source_url: str | None = Field(
        default=None,
        description="URL of the source"
    )


class RestaurantList(BaseModel):
    restaurants: list[RestaurantInfo]