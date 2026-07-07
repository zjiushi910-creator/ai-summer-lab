from pathlib import Path
import numpy as np
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
raw_data_path = project_root / "data" / "raw" / "student_scores.csv"
processed_data_path = project_root / "data" / "processed" / "student_scores_cleaned.csv"
score_columns = ["math", "english", "python"]

def fill_missing_scores(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()
    for column in score_columns:
        score_mean = cleaned_df[column].mean()
        cleaned_df[column] = cleaned_df[column].fillna(score_mean)
    return cleaned_df

def add_average_and_grade(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()
    cleaned_df["average"] = cleaned_df[score_columns].mean(axis=1).round(2)
    cleaned_df["grade"] = np.where(cleaned_df["average"] >= 85, "A",
                                   np.where(cleaned_df["average"] >= 70, "B", "C"))
    return cleaned_df

def main() -> None:
    df = pd.read_csv(raw_data_path)

    print("Original Data")
    print(df)

    df = fill_missing_scores(df)
    df = add_average_and_grade(df)

    print("\nFinal Data")
    print(df)

    df.to_csv(processed_data_path, index=False, encoding="utf-8")
    print(f"\nSaved cleaned data to: {processed_data_path}")


if __name__ == "__main__":
    main()