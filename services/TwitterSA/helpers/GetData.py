"""Get data from snscrape."""
import snscrape.modules.twitter as snt
import pandas as pd


def get_data_from_snscrape(query, max) -> pd.DataFrame:
    """Get data from snscrape lib."""
    # Get tweets
    tweets = []
    for tweet in snt.TwitterSearchScraper(query).get_items():
        tweets.append(vars(tweet))
        if len(tweets) == max:
            break

    # Set Columns
    cols = [
        "url",
        "date",
        "rawContent",
        "renderedContent",
        "id",
        "user",
        "replyCount",
        "retweetCount",
        "likeCount",
        "quoteCount",
        "conversationId",
        "lang",
        "source",
        "sourceUrl",
        "sourceLabel",
        "links",
        "media",
        "retweetedTweet",
        "quotedTweet",
        "inReplyToTweetId",
        "inReplyToUser",
        "mentionedUsers",
        "coordinates",
        "place",
        "hashtags",
        "cashtags",
        "card",
        "viewCount",
        "vibe",
    ]

    return pd.DataFrame(data=tweets, columns=cols)
