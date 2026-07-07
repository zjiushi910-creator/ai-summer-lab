from pathlib import Path
import pandas as pd
import json

from pandas import DataFrame
from src.day05_data_pipeline import fill_missing_scores

project_root = Path(__file__).resolve().parents[1]
config_path = project_root / "configs" / "day07_config.json"
raw_data_path = project_root / "data" / "raw" / "student_scores.csv"

def load_config() -> dict:
    with open(config_path, "r" , encoding="utf-8") as f:
        config = json.load(f)
    return config

def load_scores_data(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

def add_average_and_grade_from_config(
        df: pd.DataFrame,
        score_columns: list[str],
        grade_a: int,
        grade_b: int
) -> pd.DataFrame:
    result = df.copy()
    result["average"] = result[score_columns].mean(axis=1).round(1)
    result["grade"] = "C"
    result.loc[result["average"] >= grade_b, "grade"] = "B"
    result.loc[result["average"] >= grade_a, "grade"] = "A"
    return result

def main() -> None:
    config = load_config()
    df = load_scores_data(raw_data_path)

    score_columns = config["score_columns"]
    grade_a = config["grade_a"]
    grade_b = config["grade_b"]

    print(score_columns)
    print(grade_a)
    print(grade_b)

    cleaned_df = fill_missing_scores(df)
    result = add_average_and_grade_from_config(cleaned_df, score_columns, grade_a, grade_b)
    print(result)
    ground_value = result["grade"].value_counts()
    for grade, value in ground_value.items():
        print(f"{grade}:{value}")


if __name__ == "__main__":
    main()