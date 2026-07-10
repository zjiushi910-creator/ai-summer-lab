import json
import requests
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

root = Path(__file__).resolve().parents[1]
config_path = root / "configs" / "github_config.json"


class GitHubDataAnalyzer:
    def load_config(self):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
    def __init__(self):
        self.config = None
        self.load_config()
        self.username = self.config["username"]
        self.base_url = self.config["base_url"]
        self.url = f"{self.base_url}/{self.username}"
        self.data = None
        self.cleaned_data = None

    def get_data(self):
        try:
            self.data = requests.get(self.url, timeout=5)
            logging.info(f"请求成功")
        except requests.RequestException as e:
            logging.error(f"请求出错: ,{e}")

    def run(self):
        self.get_data()

a = GitHubDataAnalyzer()
a.run()


