import tweepy
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from textblob import TextBlob
from nltk.corpus import stopwords
import re
import keys as k

# Tokens de acceso
consumer_key = k.API_KEY
consumer_secret = k.API_KEY_SECRET
access_token = k.Acces_Token
access_token_secret = k.Acces_Token_Secret

# Autenticación en la API de Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define las palabras clave relevantes para buscar los tweets
palabras_clave = ["bitcoin", "BTC", "$BTC"]

# Data processing: Cleaning Tweet texts
def clean_text(new_tweet):
    ex_list = ['rt', 'http[^\s]*', 'RT', '#[^\s]*\S', '@[^\s]*:\S']
    exc = '|'.join(ex_list)
    text = re.sub(exc, '', new_tweet)
    text = text.lower()
    words = text.split()
    stopword_list = stopwords.words('english')
    words = [word for word in words if word not in stopword_list]
    clean_text = ' '.join(words)
    return clean_text

# Sentiment score analysis
def sentiment_score(new_tweet):
    analysis = TextBlob(new_tweet)
    if analysis.sentiment.polarity > 0:
        return 1  # positive
    elif analysis.sentiment.polarity == 0:
        return 0  # neutral
    else:
        return -1  # negative

# Crear clase de tabla de tweets
Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'

    tweet_id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    user_id = Column(String)
    screen_name = Column(String)
    full_name = Column(String)
    text = Column(Text)
    hashtags = Column(ARRAY(String))
    mentions = Column(ARRAY(String))
    retweet_count = Column(Integer)
    retweet_user = Column(ARRAY(String))
    favorite_count = Column(Integer)
    tweet_sentiment = Column(Integer)

# Conexión a la base de datos PostgreSQL
engine = create_engine('postgresql://<user1>:<PassTwit>@<LocalHost>:<5433>/<BitcoinTwits>')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Obtén tweets basados en las palabras clave
tweets = []
for palabra_clave in palabras_clave:
    for tweet in tweepy.Cursor(api.search_tweets, palabra_clave, count=100, tweet_mode='extended').items(100000):
        tweets.append(tweet)

# Almacena los tweets en la base de datos PostgreSQL
for tweet in tweets:
    if not tweet.full_text.startswith('RT @'):
        tweet_id
