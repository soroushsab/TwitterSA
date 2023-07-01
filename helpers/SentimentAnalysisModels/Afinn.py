from afinn import Afinn
import pandas as pd


def auto_tag(data: pd.DataFrame) -> pd.DataFrame:
    """To calculate polarity."""

    # define afinn objects
    afn = Afinn()

    # Auto tagging on data using afinn
    afinn_results: list = [afn.score(row["normalized tweet"]) for _, row in data.iterrows()]

    # Add to result data (convert the results to classification data)
    # data["Afinn"] = [1 if el > 0 else -1 if el < 0 else 0 for el in afinn_results]
    data["Afinn"] = afinn_results

    return data
