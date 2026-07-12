from src.clients.github_client import GitHubClient
from src.services.github_service import GitHubService
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
base_root = root / "configs" / "github_config.json"
with open(base_root, "r", encoding="utf-8") as f:
    data = json.load(f)

def main() -> None:
    client = GitHubClient(data["username"], data["base_url"])

    service = GitHubService(client)
    user = service.get_user()
    print(user.login)
    print(user.followers)
    print(user.public_repos)

    repos = service.get_repo()
    for repo in repos:
        print(f"Name     : {repo.name}")
        print(f"Language : {repo.language}")
        print(f"Stars    : {repo.stargazers_count}")
        print(f"Forks    : {repo.forks_count}")
        print()
if __name__ == "__main__":
    main()