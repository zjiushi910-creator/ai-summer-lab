from dataclasses import dataclass
@dataclass
class GitHubUser:
    login: str
    followers: int
    public_repos: int