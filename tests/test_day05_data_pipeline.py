import pandas as pd
from src.day05_data_pipeline import fill_missing_scores, add_average_and_grade

def test_fill_missing_scores():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Cindy"],
        "math": [90, None, 60],
        "english": [80, 70, None],
        "python": [100, 80, 60],
    })

    result = fill_missing_scores(df)

    assert result["math"].isna().sum() == 0
    assert result["english"].isna().sum() == 0
    assert result.loc[1,"math"] == 75
    assert result.loc[2,"english"] == 75

def test_add_average_and_grade():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Cindy"],
        "math": [90, 75, 60],
        "english": [90, 75, 60],
        "python": [90, 75, 60],
    })

    result = add_average_and_grade(df)

    assert result.loc[0, "average"] == 90
    assert result.loc[1, "average"] == 75
    assert result.loc[2, "average"] == 60

    assert result.loc[0, "grade"] == "A"
    assert result.loc[1, "grade"] == "B"
    assert result.loc[2, "grade"] == "C"