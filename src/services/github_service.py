from src.clients.github_client import GitHubClient
from src.models.github_user import GitHubUser
from src.models.github_repository_pydantic import GitHubRepository
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
    def build_repo(self) -> list[GitHubRepository]:
        repositories = []
        response = self.client.get_repositories()
        raw_data = response.json()
        for repo in raw_data:
            clean_repo = {
                "name": repo["name"],
                "language": repo["language"],
                "stargazers_count": repo["stargazers_count"],
                "forks_count": repo["forks_count"],
            }

            repository = GitHubRepository.model_validate(clean_repo)
            repositories.append(repository)
        return repositories

    def get_user(self):
        return  self.build_user()
    def get_repo(self):
        return self.build_repo()