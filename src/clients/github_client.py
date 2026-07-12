import requests

class GitHubClient:
    def __init__(self, username: str, base_url: str):
        self.username = username
        self.base_url = base_url

    def get_user(self) -> requests.Response:
        url = f"{self.base_url}/{self.username}"
        response = requests.get(url, timeout=5)
        return response

    def get_repositories(self) -> requests.Response:
        url = f"{self.base_url}/{self.username}/repos"
        response = requests.get(url, timeout=5)
        return response