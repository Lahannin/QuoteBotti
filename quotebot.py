# import necessary modules and login tokens
import threading
import requests
from database import *
from bs4 import BeautifulSoup as bs
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)


def get_quote():
    global tweet
    global quote
    global author

    # website with quotes images
    url = 'http://www.eduro.com/'

    # download page for parsing
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    # locate all elements with dailyquote tag
    dailyquote = soup.find('dailyquote')

    # separate quote and author of the quote
    quote = dailyquote.find('p').get_text()
    author = dailyquote.find(class_='author').get_text()

    # string for the tweet
    tweet = '"'+ quote + '"' + "" + author


def quote_bot():
    global tweet
    global quote
    global author

    # create a database for quotes
    database()

    # count nr of tweets
    tweet_count = 0

    # call function in every 3 hours
    threading.Timer(10800, quote_bot).start()
    get_quote()

    # access twitter
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret)


    # check if the tweet is no longer than 140 char and it has not been tweeted before
    if len(tweet) <= 140 and check_quote(quote):
        try:
            twitter.update_status(status=tweet)
            print("Tweeted: {}".format(tweet))
            # increase tweet_count by one
            tweet_count +=1
            # add quote to the database
            add_quote(quote, author)
            #prints tweeted quote
            print("quotebot has tweeted {} quotes".format(tweet_count))
        # if quote already tweeted, pass
        except Exception as e:
            pass
    else:
        print("Already tweeted")

# calls the function
quote_bot()
