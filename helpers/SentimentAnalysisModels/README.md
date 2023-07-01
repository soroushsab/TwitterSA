# To add model

You need to add your model (not the algorithm) to this folder as one file and make sure the main function name is "auto_tag", and it gets one argument which is data and it will return the data after adding a column to it which is the polarity result.

"data" is a data frame with one or more column(s), and the pre-processed text column is "normalized tweet".

The output will be the same data frame plus adding a new column with a name for it.

Ex:

```
def auto_tag(data: pd.DataFrame):

    # Auto tagging on data using TextBlob -> this will be your model auto tagging
    textblob_results: list = [TextBlob(row["normalized tweet"]).sentiment.polarity for _, row in data.iterrows()]

    # You will add your result to the main data like this (Please make sure you don't change any order or your code is not skipping any row)
    data["Text Blob"] = textblob_results

    return data
```
