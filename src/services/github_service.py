from src.clients.github_client import GitHubClient
from src.models.github_user import GitHubUser

class GitHubService:
    def __init__(self, client: GitHubClient):
        self.client = client
    def build_user(self) -> GitHubUser:
        response = self.client.get_user()
        raw_data = response.json()
        clean_data = {
            "login": raw_data["login"],
            "followers": raw_data["followers"],
            "public_repos": raw_data["public_repos"]
        }
        return GitHubUser(**clean_data)
    def get_user(self):
        return  self.build_user()
