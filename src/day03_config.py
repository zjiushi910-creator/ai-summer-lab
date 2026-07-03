from dataclasses import dataclass
from pathlib import Path
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

@dataclass
class AppConfig:
    project_name: str
    data_dir: str
    log_level: str
    chunk_size: int
    top_k: int

def load_config(config_path: Path) -> AppConfig:
    config_text = config_path.read_text(encoding="utf-8")
    config_dict = json.loads(config_text)
    config = AppConfig(**config_dict)
    return config

def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "configs" / "app_config.json"
    config = load_config(config_path)
    logging.info(f"Project name: {config.project_name}")
    logging.info(f"Data directory: {config.data_dir}")
    logging.info(f"Log level: {config.log_level}")
    logging.info(f"Chunk size: {config.chunk_size}")
    logging.info(f"Top K: {config.top_k}")

if __name__ == "__main__":
    main()