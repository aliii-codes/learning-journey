from pydantic import BaseModel, Field


class Restaurant(BaseModel):

    name: str = Field(
        description="Name of the restaurant"
    )

    location: str = Field(
        description="Exact location of the restaurant"
    )

    description: str = Field(
        description="Description of the restaurant"
    )

    phone_number: str | None = Field(
        default=None,
        description="Phone number of the restaurant"
    )

    special_thing: str | None = Field(
        default=None,
        description="Any special or unique thing about the restaurant"
    )


class RestaurantList(BaseModel):

    restaurants: list[Restaurant] = Field(
        description="List of restaurants found from the web search"
    )