from nrclex import NRCLex
import pandas as pd


def calculate_emotions(data: pd.DataFrame) -> pd.DataFrame:
    """To calculate polarity."""

    # define lists
    fears: list = []
    angers: list = []
    anticipations: list = []
    trusts: list = []
    surprises: list = []
    positives: list = []
    negatives: list = []
    sadnesss: list = []
    disgusts: list = []
    joys: list = []

    # calculates
    for _, row in data.iterrows():
        fears.append((NRCLex(row["normalized tweet"]).affect_frequencies)["fear"])
        angers.append((NRCLex(row["normalized tweet"]).affect_frequencies)["anger"])
        anticipations.append((NRCLex(row["normalized tweet"]).affect_frequencies)["anticipation"])
        trusts.append((NRCLex(row["normalized tweet"]).affect_frequencies)["trust"])
        surprises.append((NRCLex(row["normalized tweet"]).affect_frequencies)["surprise"])
        positives.append((NRCLex(row["normalized tweet"]).affect_frequencies)["positive"])
        negatives.append((NRCLex(row["normalized tweet"]).affect_frequencies)["negative"])
        sadnesss.append((NRCLex(row["normalized tweet"]).affect_frequencies)["sadness"])
        disgusts.append((NRCLex(row["normalized tweet"]).affect_frequencies)["disgust"])
        joys.append((NRCLex(row["normalized tweet"]).affect_frequencies)["joy"])

    # Add to result data
    data["fear"] = fears
    data["anger"] = angers
    data["anticipation"] = anticipations
    data["trust"] = trusts
    data["surprise"] = surprises
    data["positive"] = surprises
    data["negative"] = negatives
    data["sadness"] = sadnesss
    data["disgust"] = disgusts
    data["joy"] = joys

    return data
