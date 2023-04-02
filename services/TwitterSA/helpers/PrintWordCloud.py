"""Print wordcloud."""
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

from .Preprocess import text_process


def print_word_cloud(data: pd.DataFrame) -> None:
    """To print the word cloud."""
    # Create a string and define stop words
    comment_words = ""
    stopwords = set(STOPWORDS)

    # Add words to the string
    for _, row in data.iterrows():
        val = row["normalized tweet"]
        val = text_process(val)
        tokens = val.split()
        comment_words += " ".join(tokens) + " "

    # Create the opject
    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color="white",
        stopwords=stopwords,
        collocations=False,
        min_font_size=10,
    ).generate(comment_words)

    # Plot the words
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()
