import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class GitHubUserAnalyzer:
    def __init__(self, username):
        self.username = username
        self.base_url = "https://api.github.com/users"
        self.url = f"{self.base_url}/{self.username}"
        self.user_data = None

    def get_data(self):
        try:
            response = requests.get(self.url, timeout=5)
            self.user_data = response.json()
            logging.info("请求成功")
        except requests.RequestException as e:
            logging.error(f"请求失败: {e}")

    def parse_user_info(self):
        name = self.user_data["name"] or "未填写"
        bio = self.user_data["bio"] or "未填写"
        print(f"Login: {self.user_data["login"]}")
        print(f"Public_Repos: {self.user_data["public_repos"]}")
        print(f"Followers: {self.user_data["followers"]}")
        print(f"Name: {name}")
        print(f"Following: {self.user_data["following"]}")
        print(f"Created At: {self.user_data["created_at"]}")
        print(f"Bio: {bio}")
    def run(self):
        self.get_data()
        if self.user_data is not None:
            self.parse_user_info()
        else:
            print("没有可读取的数据")

def main() -> None:
    analyzer = GitHubUserAnalyzer("zjiushi910-creator")
    analyzer.run()

if __name__ == "__main__":
    main()
