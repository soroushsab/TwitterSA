"""Text process."""
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import string

# from nltk.stem import PorterStemmer


def text_process(text: str) -> str:
    """To pre process a text."""
    # Tokenize the text
    tokens = text.split(" ")

    contractions = {
        "I'm": "I am",
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he had",
        "he'd've": "he would have",
        "he'll": "he will",
        "he'll've": "he will have",
        "he's": "he is",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "how's": "how is",
        "i'd": "I would",
        "i'd've": "I would have",
        "i'll": "I will",
        "i'll've": "I will have",
        "i'm": "I am",
        "i've": "I have",
        "isn't": "is not",
        "it'd": "it would",
        "it'd've": "it would have",
        "it'll": "it will",
        "it'll've": "it will have",
        "it's": "it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd": "she would",
        "she'd've": "she would have",
        "she'll": "she will",
        "she'll've": "she will have",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "so's": "so is",
        "that'd": "that would",
        "that'd've": "that would have",
        "that's": "that is",
        "there'd": "there would",
        "there'd've": "there would have",
        "there's": "there is",
        "they'd": "they would",
        "they'd've": "they would have",
        "they'll": "they will",
        "they'll've": "they will have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        "we'd": "we would",
        "we'd've": "we would have",
        "we'll": "we will",
        "we'll've": "we will have",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what'll've": "what will have",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "when's": "when is",
        "when've": "when have",
        "where'd": "where did",
        "where's": "where is",
        "where've": "where have",
        "who'll": "who will",
        "who'll've": "who will have",
        "who's": "who is",
        "who've": "who have",
        "why's": "why is",
        "why've": "why have",
        "will've": "will have",
        "won't": "will not",
        "won't've": "will not have",
        "would've": "would have",
        "wouldn't": "would not",
        "wouldn't've": "would not have",
        "y'all": "you all",
        "y'all'd": "you all would",
        "y'all'd've": "you all would have",
        "y'all're": "you all are",
        "y'all've": "you all have",
        "you'd": "you would",
        "you'd've": "you would have",
        "you'll": "you will",
        "you'll've": "you will have",
        "you're": "you are",
        "this's": "this is",
        "you've": "you have",
    }

    # Correct broken words
    temp: list = []
    for el in tokens:
        if el in contractions:
            splited_el = contractions[el].split(" ")
            temp.extend(iter(splited_el))
        else:
            temp.append(el)
    tokens = temp

    # Re-tokenize
    text2 = "".join(f"{el} " for el in tokens)
    tokens = word_tokenize(text2)

    # Convert to lowercase
    tokens = [word.lower() for word in tokens]

    # remove to punctuation
    tokens = [
        word.translate(str.maketrans("", "", string.punctuation)) for word in tokens
    ]

    # Convert to lowercase
    tokens = [word.replace(" ", "") for word in tokens]

    # Remove stopwords and redundant words or letters
    stop_words = set(stopwords.words("english"))
    tokens = [
        el2
        for el2 in tokens
        if (el2 not in stop_words or el2 == "not")
        and not el2.startswith("http")
        and not el2.startswith("@")
        and len(el2) > 1
    ]

    # Stem the words
    # stemmer = PorterStemmer()
    # tokens = [stemmer.stem(word) for word in tokens]

    return " ".join([str(elem) for elem in tokens])


def create_data(tweets: pd.DataFrame) -> pd.DataFrame:
    """To create pre-processed data from tweets."""
    return pd.DataFrame(
        data=[text_process(row["rawContent"]) for _, row in tweets.iterrows()],
        columns=["normalized tweet"],
    )
