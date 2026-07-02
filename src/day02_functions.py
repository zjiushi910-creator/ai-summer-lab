from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def load_text_file(file_path: Path) -> str:
    text = file_path.read_text(encoding="utf-8")
    return text

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_lines(text: str) -> int:
    lines = text.splitlines()
    return len(lines)

def count_characters(text: str) -> int:
    return len(text)

def analyze_text(text: str) -> dict[str, int]:
    result = {
        "word_count": count_words(text),
        "line_count": count_lines(text),
        "character_count": count_characters(text)
    }
    return result

def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    file_path = project_root / "data" / "sample.txt"
    text = load_text_file(file_path)
    analysis = analyze_text(text)
    logging.info(f"file path: {file_path}")
    logging.info(f"Text content:\n{text}")
    logging.info(f"Analysis result: {analysis}")

if __name__ == "__main__":
    main()