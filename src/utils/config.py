from dataclasses import dataclass
from pathlib import Path
import json

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