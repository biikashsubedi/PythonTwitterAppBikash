import tweepy


def main():
    twitter_auth_keys = {
        "consumer_key": "ZiiAYBsnNDsuTVnip4ZdvmnHc",
        "consumer_secret": "JsujRBxlO7qvmJcuW4qliSea0WJpG5n7tHaKicFqsfoh55o7Fp",
        "access_token": "1189782957449347074-C8bBEL8iOUuDGl1WGl2W2X8nJhpTBM",
        "access_token_secret": "omxpdLqq0YIHnYHslEj8lWcB2bxTMcW9uDaxJZ1H1zmuB"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )

    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )

    api = tweepy.API(auth)

    """Posting Status on Twitter"""
    tweet = "Hello, this is my tweet from python Programming"
    status = api.update_status(status=tweet)

    """Searching python and getting top 10 results from Twitter"""
    search_results = api.search(q="python", count=10)
    for i in search_results:
        print(i)

    """Like on KP Oli Tweet"""
    api.create_favorite(1274577342141091840)

    """Retweet KP Oli Tweet"""
    api.retweet(1274577342141091840)

    """Making all Follower and following of KP Oli"""
    for user in tweepy.Cursor(api.followers, screen_name='kpsharmaoli').items():
        # print(user)
        print(user.screen_name)

    """Finding Trends"""
    trends_results = api.trends_place(1)
    for trends in trends_results[0]['trends']:
        print(trends['name'])

    """Creating follower, like, retweet at once which we search"""
    tweets = tweepy.Cursor(api.search, q="#covid").items(1)

    for tweet in tweets:
        print(tweet.id)
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        print(tweet.user.screen_name)
        api.create_friendship(tweet.user.screen_name)


main()
