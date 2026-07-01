from pathlib import Path
import logging
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def project_root() -> Path:
    return Path(__file__).resolve().parents[1]

def create_demo_vector() -> np.ndarray:
    vector = np.array([1.0,2.0,3.0])
    return vector

def main() -> None:
    root = project_root()
    vector = create_demo_vector()
    logging.info(f"Project root: {root}")
    logging.info(f"Demo vector: {vector}")
    logging.info(f"Vector shape: {vector.shape}")

if __name__ == "__main__":
    main()