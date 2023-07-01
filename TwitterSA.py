from typing import Union
from helpers.GetData import get_data_from_snscrape
from helpers.ReadWrite import save_data_frame, read_data_frame
from helpers.Preprocess import create_data
from helpers.CalculatePolarity import calculate_polarities
from helpers.CalculateEmotions import calculate_emotions
from helpers.PrintWordCloud import print_word_cloud
from helpers.Comparison import comparison_table


class TwitterSA:
    """We create an object of this class which is going to do all process
    with the same object. You can create an object for each query"""

    def __init__(self, query: Union[str, None] = None) -> None:
        """To initiate the object"""

        if query:
            self.set_query(query)
        else:
            self._log_message(
                """You need to call Object.setQuery("your query") or
                upload a data set using object.upload_data(isPreProcessed= True/False, "any name", "Any directory/Can be blank")."""
            )

    def __str__(self) -> str:
        """To print the object"""

        if hasattr(self, "query"):
            return f"""An object of TwitterSA to search for \n\t"{self.query}"."""
        else:
            return """You still haven't set any query for this Object."""

    def set_query(self, query: str) -> None:
        """To set the query"""

        self.query = query

    def get_data(self, max: int = 10) -> None:
        """To get the tweets"""
        self._log_message(
            "In this function you need to set max number (Object.get_data) for tweets and the default is 10. Also it depends on existence tweets"
        )

        if not hasattr(self, "query"):
            return self._log_message("""You still haven't set any query for this Object.""")
        try:
            self.tweets = get_data_from_snscrape(self.query, max)
            return None
        except Exception as e:
            return self._log_message(e)

    def upload_data(self, isPreProcessed: bool, filename: str, directory: str = "") -> None:
        """To upload the data."""
        self.tweets = read_data_frame(filename, directory)
        try:
            self.data = self.tweets if isPreProcessed else create_data(self.tweets)
        except Exception as e:
            return self._log_message(e)

    def save_to_csv(self, filename: str = "TwitterSA", directory: str = "") -> None:
        """To save the data."""

        if not hasattr(self, "tweets"):
            return self._log_message("""You still haven't download the data for this query.""")

        try:
            if not hasattr(self, "data"):
                save_data_frame(self.tweets, directory, filename)
            else:
                save_data_frame(self.data, directory, filename)
            return None
        except Exception as e:
            return self._log_message(e)

    def pre_process_text(self) -> None:
        if not hasattr(self, "tweets"):
            return self._log_message("""You still haven't download the data for this query.""")
        try:
            self.data = create_data(self.tweets)
            return None
        except Exception as e:
            return self._log_message(e)

    def calculate_polarity(self) -> None:
        """To calculate polarities."""

        if not hasattr(self, "data"):
            return self._log_message("""You still haven't preprocessed the data for this query.""")

        try:
            self.data = calculate_polarities(self.data)
        except Exception as e:
            return self._log_message(e)

    def calculate_emotions(self) -> None:
        """To calculate emotions."""

        if not hasattr(self, "data"):
            return self._log_message("""You still haven't preprocessed the data for this query.""")
        try:
            self.data = calculate_emotions(self.data)
        except Exception as e:
            return self._log_message(e)

    def compare_the_results(self) -> None:
        """To compare the results."""

        if not hasattr(self, "data"):
            return self._log_message("""You still haven't preprocessed the data for this query.""")
        if len(self.data.columns) < 4:
            return self._log_message("""DataFrame doesn't include the polarity results.""")
        try:
            self.comparisonTable = comparison_table(self.data)
        except Exception as e:
            return self._log_message(e)

    def word_cloud(self) -> None:
        """To print the word cloud"""

        if not hasattr(self, "data"):
            return self._log_message("""You still haven't preprocessed the data for this query.""")
        # Print
        print_word_cloud(self.data)
        return None

    # TODO Rename this here and in `calculate_emotions` and `word_cloud`
    def _log_message(self, message):
        print("""------------------------------------------------""")
        print(message)
        print("""------------------------------------------------""")
        return None
