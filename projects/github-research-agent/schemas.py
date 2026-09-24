from pydantic import BaseModel, Field


class RepoReport(BaseModel):
    "Report for a repository"
    name: str = Field(description="Name of the repository")
    description: str = Field(description="Description of the repository")
    language: str = Field(description="Language of the repository")
    stars: int = Field(description="Total stars of the repository")
    forks: int = Field(description="Total forks of the repository")
    summary: str = Field(description="Summary of the repository")
