from pydantic import BaseModel, Field


class RestaurantInfo(BaseModel):
    name: str
    location: str
    description: str | None = None
    phone_number: str | None = None
    special_thing: str | None = None
    source_url: str | None = None


class RestaurantNames(BaseModel):
    names: list[str] = Field(
        description="Names of all restaurants found in the research"
    )


class RestaurantList(BaseModel):
    restaurants: list[RestaurantInfo]