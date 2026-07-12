from dataclasses import dataclass

@dataclass
class GitHubRepository:
    name: str
    language: str | None
    stargazers_count: int
    forks_count: int