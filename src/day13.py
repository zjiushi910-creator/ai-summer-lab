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

if __name__ == "__main__":
    main()