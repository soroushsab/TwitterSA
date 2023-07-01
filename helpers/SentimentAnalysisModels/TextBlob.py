from textblob import TextBlob
import pandas as pd


def auto_tag(data: pd.DataFrame) -> pd.DataFrame:
    """To calculate polarity."""

    # Auto tagging on data using TextBlob
    textblob_results: list = [TextBlob(row["normalized tweet"]).sentiment.polarity for _, row in data.iterrows()]

    # Add to result data
    data["Text Blob"] = textblob_results

    return data
