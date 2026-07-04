from pathlib import Path

from utils.config import load_config
from utils.file_utils import load_text_file
from utils.logger import get_logger

def count_words(text: str) -> int:
    return len(text.split())

def count_lines(text: str) -> int:
    return len(text.splitlines())

def count_characters(text:str) -> int:
    return len(text)

def analyze_text(text: str) -> dict:
    result = {
        "words": count_words(text),
        "lines": count_lines(text),
        "characters": count_characters(text)
    }
    return result

def main() -> None:
    project_root = Path(__file__).resolve().parents[1]

    config_path = project_root / "configs" / "app_config.json"
    config = load_config(config_path)

    logger = get_logger(
        name=config.project_name,
        log_level=config.log_level,
    )

    data_path = project_root / config.data_dir / "sample.txt"
    text = load_text_file(data_path)

    analysis_result = analyze_text(text)

    logger.info(f"Text file path: {data_path}")
    logger.info(f"Text analysis result: {analysis_result}")

    print("Text Analysis Result")
    print("--------------------")
    print(f"Words: {analysis_result['words']}")
    print(f"Lines: {analysis_result['lines']}")
    print(f"Characters: {analysis_result['characters']}")

if __name__=="__main__":
    main()