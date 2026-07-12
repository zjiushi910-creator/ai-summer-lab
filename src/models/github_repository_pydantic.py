from pydantic import BaseModel, Field
class GitHubRepository(BaseModel):
    name: str = Field(min_length=3)
    language: str | None
    stargazers_count: int
    forks_count: int