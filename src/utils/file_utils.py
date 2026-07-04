from pathlib import Path

def load_text_file(file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found{file_path}")

    text = file_path.read_text(encoding="utf-8")
    return text
