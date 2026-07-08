from pathlib import Path
import json
import pandas as pd
import numpy as np
from src.day05_data_pipeline import fill_missing_scores

class ScoreAnalyzer:
    def __init__(self, config_path: Path, raw_data_path: Path):
        self.config_path = config_path
        self.raw_data_path = raw_data_path
        self.config = None
        self.df = None
        self.cleaned_df = None

    def load_config(self) -> None:
        with open(self.config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def load_data(self) -> None:
        self.df = pd.read_csv(self.raw_data_path)

    def clean_data(self) -> None:
        self.cleaned_df = fill_missing_scores(self.df)

    def add_score_and_grade(self) -> None:
        score_column = self.config["score_columns"]
        self.cleaned_df["average"] = self.cleaned_df[score_column].mean(axis=1).round(2)

        self.cleaned_df["grade"] = np.where(
            self.cleaned_df["average"] >= self.config["grade_a"],"A",np.where(
                self.cleaned_df["average"] >= self.config["grade_b"],"B","C"
            )
        )

    def run(self) -> pd.DataFrame:
        self.load_config()
        self.load_data()
        self.clean_data()
        self.add_score_and_grade()
        return self.cleaned_df

