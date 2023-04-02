"""Main file."""
from typing import Union
from .helpers.GetData import get_data_from_snscrape
from .helpers.SaveCSV import save_data_frame
from .helpers.Preprocess import create_data
from .helpers.CalculatePolarity import calculate_polarities
from .helpers.CalculateEmotions import calculate_emotions
from .helpers.PrintWordCloud import print_word_cloud


class TwitterSA:
    """Twitter Sentiment Analysis."""

    """We create an object of this class which is going to do all process
    with the same object. You can create an object for each query."""

    def __init__(self, query: Union[str, None] = None) -> None:
        """To initiate the object."""
        if query:
            self.set_query(query)
        else:
            print("""You need to call Object.setQuery("your query").""")

    def __str__(self) -> str:
        """To print the object."""
        if hasattr(self, "query"):
            return f"""An object of TwitterSA to search for \n\t"{self.query}"."""
        else:
            return """You still haven't set any query for this Object."""

    def set_query(self, query: str) -> None:
        """To set the query."""
        self.query = query

    def get_data(self, max: int = 10) -> None:
        """To get the tweets."""
        print(
            """In this function you need to set max number (Object.get_data) for tweers
              and the default is 10. Also it depends on existence tweets"""
        )

        if not hasattr(self, "query"):
            print("""You still haven't set any query for this Object.""")
            return None

        try:
            self.tweets = get_data_from_snscrape(self.query, max)
            return None
        except Exception as e:
            print(e)
            return None

    def save_to_csv(self, address: str = "", filename: str = "TwitterSA") -> None:
        """To save the data."""
        if not hasattr(self, "tweets"):
            print("""You still haven't set any query for this Object.""")
            return None

        try:
            save_data_frame(self.tweets, address, filename)
            return None
        except Exception as e:
            print(e)
            return None

    def pre_process_text(self) -> None:
        """To process the data."""
        if not hasattr(self, "tweets"):
            print("""You still haven't set any query for this Object.""")
            return None
        try:
            self.data = create_data(self.tweets)
            return None
        except Exception as e:
            print(e)
            return None

    def calculate_polarity(self) -> None:
        """To calculate polariteis."""
        if not hasattr(self, "data"):
            print("""You still haven't set any query for this Object.""")
            return None

        try:
            self.data = calculate_polarities(self.data)
        except Exception as e:
            print(e)
            return None

    def calculate_emotions(self) -> None:
        """To calculate emotions."""
        if not hasattr(self, "data"):
            print("""You still haven't set any query for this Object.""")
            return None

        try:
            self.data = calculate_emotions(self.data)
        except Exception as e:
            print(e)
            return None

    def word_cloud(self) -> None:
        """To print the word cloud."""
        if not hasattr(self, "data"):
            print("""You still haven't set any query for this Object.""")
            return None

        # Print
        print_word_cloud(self.data)
        return None
