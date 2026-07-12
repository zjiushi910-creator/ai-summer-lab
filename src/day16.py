from src.models.github_repository_pydantic import GitHubRepository

repo = GitHubRepository(
    name="AI Summer Lab",
    language="Python",
    stargazers_count=18,
    forks_count=20,
)

print(repo)
print(type(repo.stargazers_count))