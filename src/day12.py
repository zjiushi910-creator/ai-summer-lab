from src.day11_github_config import GitHubDataAnalyzer

def main() -> None:
    analyzer = GitHubDataAnalyzer()
    user = analyzer.run()
    print(user.login)
    print(user.followers)
    print(user.public_repos)

if __name__ == "__main__":
    main()