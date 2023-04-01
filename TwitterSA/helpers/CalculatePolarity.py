from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from afinn import Afinn
import pandas as pd


def calculate_polarities(data: pd.DataFrame) -> pd.DataFrame:
    """To calculate polarity."""

    # define afinn and vader objects
    afn = Afinn()
    sid_obj = SentimentIntensityAnalyzer()

    # define lists
    textblob_results: list = []
    afinn_results: list = []
    vader_results: list = []

    # calculates
    for _, row in data.iterrows():
        textblob_results.append(TextBlob(row["normalized tweet"]).sentiment.polarity)
        afinn_results.append(afn.score(row["normalized tweet"]))
        vader_results.append(sid_obj.polarity_scores(row["normalized tweet"])["compound"])

    # Add to result data
    data["Text Blob"] = textblob_results
    data["Afinn"] = textblob_results
    data["Vader"] = textblob_results

    return data
