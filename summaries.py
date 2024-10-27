import pandas as pd


def format_seconds(seconds: float) -> str:
    h = int(seconds / 3600)
    m = int((seconds % 3600) / 60)
    s = int(seconds % 60)
    return f"{h:02}:{m:02}:{s:02}"


def reindex_days(series: pd.Series):
    "Given a series where the index is 1-7, remaps the index inplace to full weekdays"
    series.index = series.index.map({
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    })
