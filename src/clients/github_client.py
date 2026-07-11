import requests

class GitHubClient:
    def __init__(self, username: str, base_url: str):
        self.username = username
        self.base_url = base_url
        self.url = f"{self.base_url}/{self.username}"
    def get_user(self) -> requests.Response:
        response = requests.get(self.url, timeout=5)
        return response
