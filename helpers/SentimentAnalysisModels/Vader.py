from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


def auto_tag(data: pd.DataFrame) -> pd.DataFrame:
    """To calculate polarity."""

    # define vader objects
    sid_obj = SentimentIntensityAnalyzer()

    # Auto tagging on data using Vader
    vader_results: list = [sid_obj.polarity_scores(row["normalized tweet"])["compound"] for _, row in data.iterrows()]

    # Add to result data
    data["Vader"] = vader_results

    return data
