# Twitter Sentiment Analyzer

This is a python library that gathered a few number of useful packages and to make the process of twitter sentiment analysis (from getting the tweets) more structured.

This project is not the best but I will be more than happy to invite you to contribute and improve this package.

I tried to follow the standards of programming so it will be easy to understand and extend

NOTE:
IT IS IMPORTANT TO KNOW THIS PACKAGE IS BASICALLY WORKING WITH OTHER PYTHON LIBRARIES. SO IT IS MOSTLY DEPEND ON THEM AND IF THERE IS AN ISSUE FROM THEM YOU MAY FACE ISSUE USING THIS CLASS.

## Getting Started

### Prerequisites

Before using this you need to install Prerequisites in requirement.txt.

### Installation

...!

## Usage

Download the repo into your python file directory.

Try to import it in this way:

```
from TwitterSA.TwitterSA import TwitterSA
```

Create an object:

```
object = TwitterSA()
```

Try to add a query:

```
object.set_query("Any thing")
```

How to create a query:
https://help.twitter.com/en/using-twitter/twitter-advanced-search

Try to get data:
max is the max number of tweets that you want to get from twitter. The default is 10.

```
object.get_data(10)
```

You can save the data anywhere with any name you want as a csv file:

```
object.save_to_csv("any name", "Any directory")
```

On top of that, you can read a csv data:
NOTE: data needs to have only a column for plain texts, and it can also have the actual polarity number.

```
object.upload_data(isPreProcessed= True/False, "any name", "Any directory")
```

isPreProcessed will True if your data is already normalized and the text column name should be "normalized tweet"
isPreProcessed will False if your data is not normalized and the text column name should be "rawContent"

This is the step to do the pre processing, is is mandatory unless you want to change it in the code:

```
object.pre_process_text()
```

This is to calculate the polarity of each tweet based on three libraries:

- Text-Blob: https://pypi.org/project/textblob/
- Vader: https://pypi.org/project/vaderSentiment/#:~:text=VADER%20(Valence%20Aware%20Dictionary%20and,on%20texts%20from%20other%20domains.
- Afinn: https://pypi.org/project/afinn/

```
object.calculate_polarity()
```

This is to calculate the emotions of each tweet based on three libraries:

- NRCLex: https://pypi.org/project/NRCLex/

```
object.calculate_emotions()
```

## Contributing

You can create your branch and try to add or modify anything you want. When you want to add it to master just raise a merge and I will review it and add it to the master.

## License

No License yet.
